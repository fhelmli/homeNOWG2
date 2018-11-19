import sys
sys.path.append('devices')
import deviceBase
import deviceTempHum



import svgmanager

class hmdevicedb:
	svgManager=[]
	def __init__(self,svgManager):
		print ('hmdevicedb')
		self.svgManager=svgManager
	def getSVGClass(self,hmdevices):
		if hmdevice=='HM-WDS10-TH-O':
			return deviceTempHum(self.svgManager)
		return None
