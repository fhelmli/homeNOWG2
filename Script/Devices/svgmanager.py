#loading of svgs

import exceptions


#lazzy loading needes to be implememt3d
#todo berk thomas
class svgManager():
	svgs=[]
	
	def __init__(self):
		print('svgmanager constructor')
	
	def getSvg(self,index):
		if index<len(self.svgs):
			return self.svgs[index]
		else:
			loadSvg(self,index)
			#raise ValueError('svgmanager: wrong index used')
			#load!!
			
	
	def loadSvg(self,index):
		print('svg manager load svgs ')
		
	def print2(self):
		print('svg manager print: '+str(len(self.svgs)))
	
def test():
	print('svg manager test')
	man=svgManager()
	man.print2()
	man.loadSvg(1)
	man.print2()
	man.getSvg(1)
#test()
