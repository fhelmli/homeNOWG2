#polling
#construction of structure
#generation of svg classes

import hmccu


class model:
	ccu=[]
	deviceClasses=[]
	
	def __init__(self,ccu):
		print('model constructor')
		self.ccu=ccu
		self.ccu.updateConfig()
	
	def generateDeviceClasses(self):
		print ('model generate device classes')
		print('e  '+str(self.ccu.devices))
		#for id,name,type in self.ccu.devices.iteritems():
		#	print('element')
		# 
		
	def update(deviceindices):
		print('model update')
		for id in deviceindices:
			print('id ',id)
	
	def print(self):
		print('model: deviceclasses: '+len(self.deviceClasses))
	
def test():
	print ('model test')

#test()
		
