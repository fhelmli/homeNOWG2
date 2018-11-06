import hmdevices
import hmdevice
import settings
import hminterface

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
	s=settings.settings(1)
	i=hminterface.hmInterface(s.url())
	myhmccu=hmCCU(i)
	mydevices=hmdevices.hmDevices()
	mydev=hmdevice.hmDevice(1)
	mydevices.add(mydev)
	myhmccu.devices=mydevices
	myhmccu.print()
	myhmccu.updateValues()
	
test()
