import deviceBase
import svgmanager

class deviceTempHum(deviceBase.deviceBase):
	mySvgManager=0
	def __init__(self,mySvgManager):
		print ('deviceTempHum constructor')
		self.mySvgManager=mySvgManager
		#load svg
		self.svg=self.mySvgManager.getSvg(1)
		
	def updateValues():
		print ('deviceTempHum  updatevalues')
		
	def print2():
		print('device temphum: ')
	

def test():
	print('devicebase test')
	tempHum = deviceTempHum()

test()
	
