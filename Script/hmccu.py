import hmdevices
import hmdevice

class hmCCU:
	devices=[]
	rooms=[]
	sections=[]
	
	name=''
	interface=''
	
	def __init__(self,interface=None):
		print('hmccu constructor: ')
		self.interface=interface
	def updateConfig():
		print('hmccu update config: ')
		if self.interface==None:
			raise Exception('hmccu: no interface defined!')
		
		#update rooms
		#update sections
		#update devices
		
	def updateValues(self):
		print('hmccu update values: ')
		if self.interface==None:
			raise Exception('hmccu: no interface defined!')
		for element in self.devices.devices:
			element.print()
			element.update(self.interface)
	def print(self):
		print('hmccu  print: ')
		self.devices.print()
		print(self.rooms)
		print(self.sections)





def test():
	print('hmccu  test: ')
	myhmccu=hmCCU()
	mydevices=hmdevices.hmDevices()
	mydev=hmdevice.hmDevice()
	mydevices.add(mydev)
	myhmccu.devices=mydevices
	myhmccu.print()
	
test()
