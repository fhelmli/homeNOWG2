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
	
	#the content
	value=0
	#default 0 nix
	#defauöt 1 gerät in franz graz
	#default 2 gerät in franz lamperstätten
	def __init__(self,default=0):
		print('hmdevice constructor:')
		self.name=''
		#self.interface=interface
		if default==1:
			self.serial='KEQ0909042'
			self.port='4'
			self.key='SET_TEMPERATURE'
		if default==2:
			self.serial='LEQ0782212'
			self.port='4'
			self.key='SET_TEMPERATURE'
	
	#type 0 update by serial
	#type 1 update by id
	def update(self,interface,type=0):
		if interface==None:
			print('interface: '+str(interface))
			raise Exception('hmdevice: no interface defined!')
		if type==0: #with serial
			self.value= interface.update(self.serial,self.port,self.key)
		if type==1: #with id
			self.value=interface.updateId(self.id)
	
	def print(self):
		print('hmdevice print name: '+self.name+' serial: ' +self.serial+':'+self.port+':'+self.key+ ' room: '+str(self.room)+' section: '+str(self.section))
		print('  value: '+str(self.value))





def test():
	print('hmdevice test: ')
	s=settings.settings(2)
	interface = hminterface.hmInterface(s.url())
	
	mydev=hmDevice(2)
	#mydev.serial='KEQ0909042'
	#mydev.port='4'
	#mydev.key='SET_TEMPERATURE'
	mydev.print()
	mydev.update(interface,1)
	mydev.print()
	
test()
