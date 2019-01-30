import deviceBase
import svgmanager

class deviceContact(deviceBase.deviceBase):
	#0 means open, 1 mean close
	state=0
	bat =[]
	
	def __init__(self,mySvgManager,deviceObj):
		deviceBase.deviceBase.__init__(self,mySvgManager,deviceObj)

	@staticmethod
	def getDeviceType():
		return 'HMIP-SWDO'

	def updateValues(self):
		print ('deviceContact updatevalues')
		
		self.state = self.interface.updateWithTend(self.adr,'1','STATE')
		#batString = self.interface.update(self.adr,'0','LOW_BAT')
		#print('bat string: ' + str(batString))
		#batValue = float(batString)
		#print(batValue)
		#self.bat=batValue
		
		#update(self,serial,port,key,what='Value'):
		print(self)
	
	def __str__(self):
		return 'state: '+str(self.state)+' bat: '+str(self.bat)
