# this is old stuff


import hmdevice


class hmDevices:
	devices=[]
	def __init__(self):
		print('hmdevices constructor: ')
	def add(self,device):
		self.devices.append(device)
	def update(self,interface):
		for hmDeviceElement in self.devices:
			hmDeviceElement.update(interface)
	def printc(self):
		print('hmdevices print: len: '+str(len(self.devices)))
		for hmDeviceElement in self.devices:
			hmDeviceElement.printc()
			
def test():
	print('hmdevices test: ')
	#interface = hminterface.hmInterface('10.0.0.1')
	mydevices=hmDevices()
	dev=hmdevice.hmDevice()
	dev.printc()
	mydevices.add(dev)
	mydevices.add(dev)
	mydevices.printc()
	#mydevices.update()
	
#test()
