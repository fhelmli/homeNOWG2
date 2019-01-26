# this is old stuff


# this class handles all hm devoces and sys vars
import hminterface
import settings

class hmDevice:
	
	#0.... device    1... sysvar
	sysvar=0
	
	#name eg  regler
	name=''
	
	#serial
	serial=''
	
	# 1 2 or 4
	port=''
	
	#eg TEMPERATURE
	key=''
	
	#eg toilet
	room=0
	
	#eg light, heating
	section=0
	
	id=0
	
	#device type: welcher aktor typ ist es
	deviceType=0
	
	#the content
	actualValue=0
	lastValue=0
	tendence=0
	
	#default 0 nix
	#default 1 geraet in franz graz
	#default 2 geraet in franz lamperstaetten
	def __init__(self,default=0):
		print('hmdevice constructor:')
		self.name=''
		#self.interface=interface
		if default==1:
			self.serial='KEQ0909042'
			self.port='4'
			self.key='ACTUAL_TEMPERATURE'
		if default==2:
			self.serial='LEQ0782212'
			self.port='4'
			self.key='ACTUAL_TEMPERATURE'
			
	def updateIdFromSerial(self,interface):
		if interface==None:
			print('interface: '+str(interface))
			raise Exception('hmdevice: no interface defined!')
		self.id= interface.update(self.serial,self.port,self.key,'ID')
	
	#type 0 update by serial
	#type 1 update by id
	def update(self,interface,updateType=0):
		if interface==None:
			print('interface: '+str(interface))
			raise Exception('hmdevice: no interface defined!')
		if updateType==0: #with serial
			self.actualValue= interface.update(self.serial,self.port,self.key)
			self.lastValue= interface.update(self.serial,self.port,self.key,'LastValue')
		if updateType==1: #with id
			self.actualValue=interface.updateId(self.id)
			self.lastValue=interface.updateId(self.id,'LastValue')
		
		if type(self.actualValue)==float or type(self.actualValue)==int:
			self.tendence=self.actualValue-self.lastValue
		else:
			self.tendence=0
	
	def printc(self):
		print('hmdevice print name: '+self.name+' serial: ' +self.serial+':'+self.port+':'+self.key+ ' room: '+str(self.room)+' section: '+str(self.section) + ' id: '+str(self.id))
		print('  value: '+str(self.actualValue)+' before: '+str(self.lastValue) + ' t: '+str(self.tendence))





if __name__ == "__main__":
	print('hmdevice test: ')
	s=settings.settings(1)
	interface = hminterface.hmInterface(s.url(),1)
	
	mydev=hmDevice(1)
	mydev.printc()
	mydev.update(interface,0)
	mydev.printc()
	mydev.updateIdFromSerial(interface)
	mydev.printc()
