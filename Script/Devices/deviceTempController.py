import deviceBase
import svgmanager

class deviceTempController(deviceBase.deviceBase):
	actualTemp=[]
	setTemp=[]
	mode=[]
	bat =[]
	
	def __init__(self,mySvgManager,deviceObj):
		deviceBase.deviceBase.__init__(self,mySvgManager,deviceObj)

	@staticmethod
	def getDeviceType():
		return 'HM-CC-RT-DN'

	def updateValues(self):
		print ('deviceTempController updatevalues')
		
		self.actualTemp=self.interface.updateWithTend(self.adr,'4','ACTUAL_TEMPERATURE')
		self.setTemp=self.interface.updateWithTend(self.adr,'4','SET_TEMPERATURE')
		self.mode = self.interface.updateWithTend(self.adr,'4','CONTROL_MODE')
		batString = self.interface.updateWithTend(self.adr,'4','BATTERY_STATE')
		batValue = float(batString['value'])
		self.bat=(batValue-1.5)/(4.6-1.5)
		#update(self,serial,port,key,what='Value'):
		print(self)
	
	def __str__(self):
		return 'actualTemp: '+str(self.actualTemp)+' setTemp: '+str(self.setTemp)+' mode: '+str(self.mode)+' bat: '+str(self.bat)
