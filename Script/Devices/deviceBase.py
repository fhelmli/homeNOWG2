class deviceBase:
	svg='' #link to the real svg
	id=0  #homematic id
	deviceObj=[]  #json obj
	interface=[]  # link to the interface
	mySvgManager=0
	adr=0
	
	#def __init__(self):
	#	print('svgdevicebase constructor')
		
	def __init__(self,mySvgManager,deviceObj):
		print ('svgdevicebase constructor')
		self.mySvgManager=mySvgManager
		#load svg
		#self.svg=self.mySvgManager.getSvg(1)
		self.deviceObj=deviceObj
		self.updateAdr()
	
	def svgLink(self):
		return svg
	def getDeviceType():
		return ''
	def updateValues(self):
		return False
	def updateAdr(self):
		print(' obj: '+str(self.deviceObj))
		for key,value in self.deviceObj.iteritems():
			print('     key: '+str(key)+' val: '+str(value))
		self.adr=self.deviceObj['Address']
		print('adr: '+self.adr)  #self.interface.getResultFromScript()
		
		
		
