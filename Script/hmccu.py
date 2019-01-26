import hmdevices
import hmdevice
import settings
import hminterface
import json

import hmscripts






scriptRooms=            'var objIDs = dom.GetObject(ID_ROOMS).EnumUsedIDs();\n'
scriptRooms=scriptRooms+'string id;\n'
scriptRooms=scriptRooms+'! Alle Datenpunkte durchlaufen\n'
scriptRooms=scriptRooms+'foreach(id, objIDs){\n'
scriptRooms=scriptRooms+'  ! Einzelnen Datenpunkt holen\n'
scriptRooms=scriptRooms+'  var object = dom.GetObject(id);\n'
scriptRooms=scriptRooms+'  ! Namen und Wert des Elements ausgeben\n'
scriptRooms=scriptRooms+'  WriteLine("Name: " # object.Name() # ": " #  object.ID());\n'
scriptRooms=scriptRooms+'}'

class hmCCU:
	devicesObj=[]
	roomsObj=[]
	functionsObj=[]
	
	name=''
	interface=''
	
	def __init__(self,interface=None):
		print('hmccu constructor: ')
		self.interface=interface
	
	def updateConfig(self):
		print('hmccu update config: ')
		if self.interface==None:
			raise Exception('hmccu: no interface defined!')
		
		self.updateRooms()
		self.updateFunctions()
		self.updateDevices()
		
		print('hmccu update config done')
		

	def updateDevices(self):
		print('hmccu update    devices: ')
		result=self.interface.getResultFromScript(hmscripts.g_devicesScript)
		result=result[0:result.find('<xml')]
		#print(result)
		self.deviceObj=json.loads(result)
		#self.deviceObj.
		print(str(self.devicesObj))
		
		#for id, device in devices.iteritems():
		#		use the variable id (Key) and the 3 members of a device (Value):
		#		device["Name"], device["Interface"]+"."+device["Address"] and device["HssType"]
		
		for key, val in  self.deviceObj.iteritems():
			print('key '+str(key)+' value: '+str(val)+' adr: ')#+val[adress])
			#print(type(val))
			for k,v in val.iteritems():
				print('          key: '+str(k)+' val: '+str(v))
		#device obj aufbaen
		print (' hmccu update    devices end')
		
		
	def updateFunctions(self):
		print('hmccu update   functions: ')
		result=self.interface.getResultFromScript(hmscripts.g_functionsScript)
		result=result[0:result.find('<xml')]
		print(result)
		self.functionsObj=json.loads(result)
		print ('hmccu update   functions end')
	
	def updateRooms(self):
		print('hmccu update  rooms: ')
		result=self.interface.getResultFromScript(hmscripts.g_roomsScript)
		result=result[0:result.find('<xml')]
		print(result)
		self.roomObj=json.loads(result)
		print ('hmccu update rooms end')
		
	def updateRoomsOld(self):
		print('hmccu update  rooms: ')
		result=self.interface.getResultFromScript(scriptRooms)
		#print(result)
		lineList=result.split('\n')
		for line in lineList:
			wordList=line.split()
			roomName=wordList[1]
			roomId=wordList[2]
			print(roomName)
			print(roomId)
		#print (reslist)
		print ('end')
		
		
	def updateValues(self):
		print('hmccu update values: ')
		if self.interface==None:
			raise Exception('hmccu: no interface defined!')
		for element in self.devices.devices:
			element.printc()
			element.update(self.interface)
	
	def printc(self):
		print('hmccu  print: ')
		self.devices.printc()
		print(self.rooms)
		print(self.sections)





if __name__ == "__main__":
	print('hmccu  test: ')
	s=settings.settings(1)
	i=hminterface.hmInterface(s)
	myhmccu=hmCCU(i)

	
	#def find_between( s, start, end ):
	#return s[s.find(start)+len(start):s.rfind(end)]       
	
	myhmccu.updateConfig()
	
	
	#mydevices=hmdevices.hmDevices()
	#mydev=hmdevice.hmDevice(1)
	#mydevices.add(mydev)
	#myhmccu.devices=mydevices
	#myhmccu.printc()
	#myhmccu.updateValues()
	
#test()
