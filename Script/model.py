#polling
#construction of structure
#generation of svg classes

import hmccu
import hmdevicedb

class model:
	ccu=[]
	deviceClasses=[]
	devicedb=[]
	svgmanager=[]
	
	def __init__(self,ccu):
		print('model constructor')
		self.ccu=ccu
		self.devicedb=hmdevicedb.hmDeviceDB(None)
		#self.svgManager=
		#self.ccu.updateConfig()
	
	def generateDeviceClasses(self):
		print ('model generate device classes')
		#for id, device in devices.iteritems():
		#		use the variable id (Key) and the 3 members of a device (Value):
		#		device["Name"], device["Interface"]+"."+device["Address"] and device["HssType"]

		for id,device in self.ccu.deviceObj.iteritems():
			#	print('element')
			print('key '+str(id)+' value: '+str(device))
			print('type: ' + str(type(device)))
			print('hsstype: '+str(device['HssType']))
			devicetype=device['HssType']
			deviceclass=self.devicedb.getSVGClass(devicetype,device,self.ccu)
			#deviceclass.interface=self.ccu.interface
			if deviceclass!=None:
				self.deviceClasses.append(deviceclass)
			else:
				print('not inserted')
			
		
		
	def prepareViewController(self):
		print('ggg')
		
	def updateAll(self):
		print('model update')
		for device in self.deviceClasses:
			device.updateValues()
		print('model update end')
		
	def update(self,deviceindices):
		print('model update')
		#local indizes
		#for id in deviceindices:
			#print('id ',id)
			#self.deviceClasses[id].update()
		
		#print('model update done')
	
	def printc(self):
		print('model: deviceclasses: '+str(len(self.deviceClasses)))
	
	
	
	
if __name__ == "__main__":
	print ('model test')
