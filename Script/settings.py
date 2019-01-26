import logging
import console

class settings:
	localIp=""
	localUsername=''
	localPassword=''
	
	language="en"
	
	# 0... auto
	# 1... local ip
	# 2... cloudmatic
	# 3... rp
	# 4... homenow server
	connectionType=0
	
	#time in sec between pollings
	pollingTime=0
	
	commTimeout=15
	
	colorSchema=0
	
	debug=0
	
	#default=0...nix
	#default=1... franz graz
	#default=2... franz lamperstaetten
	def __init__(self,default=0):
		console.clear()
		print("settings constructor:")
		logging.info('settings constructor')
		self.ip="10.0.0.1"
		self.connectionType=0
		self.pollingTime=5
		self.commTimeout=10
		self.debug=1
		if default==1:
			self.localIp='http://10.0.0.1:8181/Test.exe'
			self.localUsername='admin'
			self.localPassword=''
		if default==2:
			self.localIp='http://10.0.0.2:8181/Test.exe'
			self.localUsername = 'admin'
			self.localPassword = 'cool2piktm'
	
	def url(self):
		return self.localIp
	def username(self):
		return self.localUsername
	def password(self):
		return self.localPassword
	
	def printc(self):
		print("settings print:")
		print("  ip: "+self.localIp + ' l: '+self.localUsername + ' p: '+self.localPassword)
		print("  connectiontype: "+str(self.connectionType))
		print("  pollingtime: "+str(self.pollingTime))
	
def test():
	print("test function of setting:")
	mysettings =settings()
	mysettings.printc()
	
#test()
