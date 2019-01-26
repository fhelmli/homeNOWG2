import sys
sys.path.append('Devices')
import deviceBase
import deviceTempHum
import deviceTempController
import hmccu


import svgmanager

class hmDeviceDB:
	svgManager=[]
	def __init__(self,svgManager):
		print ('hmdevicedb')
		self.svgManager=svgManager
		
		
		deviceTempHum
		
	
	def getSVGClass(self,hmdevice,deviceObj,ccu):
		print('hmdevicedb getsvgclass ask for: '+str(hmdevice))
		if hmdevice==deviceTempHum.deviceTempHum.getDeviceType():
			print('found!!')
			obj=deviceTempHum.deviceTempHum(self.svgManager,deviceObj)
			obj.interface=ccu.interface
			return obj
		if hmdevice==deviceTempController.deviceTempController.getDeviceType():
			print('found!!')
			obj=deviceTempController.deviceTempController(self.svgManager,deviceObj)
			obj.interface=ccu.interface
			return obj
		return None
