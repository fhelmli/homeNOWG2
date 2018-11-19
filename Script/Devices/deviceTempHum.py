import deviceBase
import svgmanager

class deviceTempHum(deviceBase.deviceBase):
	mySvgManager=0  # muss nach base wandern
	temp=0
	hum=0
	
	def __init__(self,mySvgManager,deviceObj):
		print ('deviceTempHum constructor')
		self.mySvgManager=mySvgManager
		#load svg
		self.svg=self.mySvgManager.getSvg(1)
		self.deviceObj=deviceObj
		
	def updateValues():
		print ('deviceTempHum  updatevalues')
		self.interface.getResultFromScript()
		
	def print2():
		print('device temphum: ')
	

def test():
	print('devicebase test')
	tempHum = deviceTempHum(None)

#test()
	
