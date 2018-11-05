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
	def print(self):
		print('hmdevices print: len: '+str(len(self.devices)))
		for hmDeviceElement in self.devices:
			hmDeviceElement.print()
			
def test():
	print('hmdevices test: ')
	#interface = hminterface.hmInterface('10.0.0.1')
	mydevices=hmDevices()
	dev=hmdevice.hmDevice()
	dev.print()
	mydevices.add(dev)
	mydevices.add(dev)
	mydevices.print()
	#mydevices.update()
	
#test()
