import deviceBase
import svgmanager

class deviceTempHum(deviceBase.deviceBase):
	temp=[]
	lastTemp=[]
	
	
	def __init__(self,mySvgManager,deviceObj):
		print ('deviceTempHum constructor')
		self.mySvgManager=mySvgManager
		#load svg
		#self.svg=self.mySvgManager.getSvg(1)
		self.deviceObj=deviceObj
		self.updateAdr()
		
	@staticmethod
	def getDeviceType():
		return 'HM-WDS10-TH-O'

	def updateValues(self):
		print ('deviceTempHum  updatevalues')
		
		self.temp= self.interface.updateWithTend(self.adr,'1','TEMPERATURE')
		self.hum=self.interface.updateWithTend(self.adr,'1','HUMIDITY')
		#update(self,serial,port,key,what='Value'):
		self.print2()
		
	def print2(self):
		print('device temphum: '+str(self.temp)+'c '+str(self.hum)+'%')
	

def test():
	print('devicebase test')
	tempHum = deviceTempHum(None)

#test()
	
