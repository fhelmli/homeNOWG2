import logging
import xml.etree.ElementTree as ET		

#import urllib.request
import urllib2

import base64
import random
import json


import settings

#link https://www.debacher.de/wiki/Homematic

debug = False

def find_between( s, start, end ):
    return s[s.find(start)+len(start):s.rfind(end)]



def getSysVarValue(url,name):
    # nur eine Variable darf gesetzt werden, diese wird automatisch im XML returniert, ohne WriteLine
    hmScript = 'mySysVar=dom.GetObject("'
    hmScript = hmScript + name + '").Value();'

    #print("script: "+hmScript)

    url = "http://" + url + ":8181/Test.exe?" + hmScript
    username = 'franzhelmli2'
    password = 'cool2pi'

    # http get request with Basic Authentication
    req = urllib.request.Request(url)

    credentials = ('%s:%s' % (username, password))
    encoded_credentials = base64.b64encode(credentials.encode('ascii'))
    req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))

    text = urllib.request.urlopen(req).read()

    # cut out the result from the returned XML
    value = find_between(str(text), '<mySysVar>', '</mySysVar>')

    print('Answer from HM Script ('+name+') :' + value)
    
    return value

def getValue(url,device,number,what):
    # nur eine Variable darf gesetzt werden, diese wird automatisch im XML returniert, ohne WriteLine
    hmScript = 'mySysVar=dom.GetObject("BidCos-RF.'
    hmScript = hmScript + device + ':' + number + '.' + what + '").Value();'

    #url = "https://home.peissl.at/rega/Test.exe?" + hmScript
    #username = 'tberk'
    #password = 'tom1977'

    url = "http://" + url + ":8181/Test.exe?" + hmScript
    
    #print('url: '+url)
    username = 'franzhelmli2'
    password = 'cool2pi'

    username='admin'
    password=''
    # http get request with Basic Authentication
    req = urllib.request.Request(url)

    credentials = ('%s:%s' % (username, password))
    encoded_credentials = base64.b64encode(credentials.encode('ascii'))
    req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))

    text = urllib.request.urlopen(req).read()
    
    #print('text: '+str(text))

    # cut out the result from the returned XML
    variableContents = find_between(str(text), '<mySysVar>', '</mySysVar>')

    print('Answer from HM Script: ' + variableContents)
    
    return variableContents


def executeHMScript(url, username,password,script):
    hmScript = script
    
    #username = 'admin'
    #password = 'cool2piktm'
    #url = "http://10.0.0.2:8181/Test.exe"

    #url = "http://" + url + ":8181/Test.exe?" + hmScript
    
    #print('url: '+url)
    #username = 'franzhelmli2'
    #password = 'cool2pi'
    
    #username='admin'
    #password=''
    
    credentials = ('%s:%s' % (username, password))
    encoded_credentials = base64.b64encode(credentials.encode('ascii'))

    post = hmScript  #urlencode(hmScript)
    req = urllib2.Request(url, post)
    req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
    response = urllib2.urlopen(req,timeout=16).read()
    
    #print response
    
    return response
    
    
def ping(host):
	"""
	Returns True if host responds to a ping request
	"""
	import subprocess, platform

	# Ping parameters as function of OS
	ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
	args = "ping " + " " + ping_str + " " + host
	need_sh = False if  platform.system().lower()=="windows" else True

	# Ping
	return subprocess.call(args, shell=need_sh) == 0

def ping2(adr):
	import os
	hostname = adr # "google.com" #example
	response = os.system("ping -c 1 " + hostname)

	#and then check the response...
	if response == 0:
		print hostname, 'is up!'
		return 1
	else:
		print hostname, 'is down!'
		return 0

#returns if a string has a number
def isaNumber(a):
	number = 0
	try:
		val = float(a)
		number =1
	except:
		number = 0
	return number

class hmInterface:
	settings=[]
	demo=0
	connected=0
	def __init__(self,mySettings,demo=0):
		print("hminterface constructor")
		self.demo=demo
		self.settings=mySettings
		self.connected = 1#ping2(self.settings.url())
		#test interface
	
	def getResultFromScript(self,script):
		if self.demo==1:
			return random.randrange(10,40)
		if self.connected==0:
			raise Exception('no connection!!')
		#return executeHMScript(self.settings.url(),self.settings.username(),self.settings.password(),script)
		
		
		credentials = ('%s:%s' % (self.settings.username(), self.settings.password()))
		encoded_credentials = base64.b64encode(credentials.encode('ascii'))

		post = script #urlencode(hmScript)
		req = urllib2.Request(self.settings.url(), post)
		req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
		response = urllib2.urlopen(req,timeout=self.settings.commTimeout).read()

		return response
		
		
		
		
		
		url = "http://" + self.url + ":8181/Test.exe?" +script
		#print('url: '+url)
		username = 'franzhelmli2'
		password = 'cool2pi'

		username='admin'
		password=''
		# http get request with Basic Authentication
		req = urllib.request.Request(url)

		credentials = ('%s:%s' % (username, password))
		encoded_credentials = base64.b64encode(credentials.encode('ascii'))
		req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))

		text = urllib.request.urlopen(req).read()
		#print('text: '+str(text))
		return text
		# cut out the result from the returned XML
		#variableContents = find_between(str(text), '<mySysVar>', '</mySysVar>')

		#print('Answer from HM Script: ' + variableContents)

		#return variableContents
	
	#what value or lastvalue
	def updateId(self,id,what='Value'):
		if self.connected==0:
			raise Exception('no connection!!')
			
		print ('hm interface updateid id: '+str(id))
		if self.demo==1:
			return random.randrange(10,40)
		script='mySysVar=dom.GetObject(' + str(id) + ').' + what + '();'
		val=self.getResultFromScript(script)
		res = find_between(str(val), '<mySysVar>', '</mySysVar>')
		return res
	
	#serial must contain also interface!!!!
	#example: hmip.023902390 
	#example: bidcos-rf.heq0232323
	def update(self,serial,port,key,what='Value'):
		#print ('hm interface updateid normal: '+str(serial)+' '+str(port)+' '+str(key))

		if self.demo==1:
			return random.randrange(10,40)
		if self.connected==0:
			raise Exception('no connection!!')
		script = 'mySysVar=dom.GetObject("'
		script = script + serial + ':' +  port + '.' +  key +'"'
		script = script + ').' + what + '();'
		
		val=self.getResultFromScript(script)
		#print ('val: '+ str(val))
		res = find_between(str(val), '<mySysVar>', '</mySysVar>')
		#print('res: '+str(res))
		return res

	def updateWithTend(self,serial,port,key):
		if self.connected==0:
			raise Exception('no connection!!')
		val=self.update(serial,port,key,'Value')
		lastVal=self.update(serial,port,key,'LastValue')
		tendence=0
		try:
			tendence=float(val)-float(lastVal)
		except:
			tendence=0
		dict={'value':val,'lastValue':lastVal,'tendence':tendence}
		return dict
			
		
	def generateDeviceList(self):
		print('hminterface generate device list')
	
	def printc(self):
		print('hminterface print: connected: '+str(self.connected))





if __name__ == "__main__":
	print('hminterface test: ')
	#res=getValue('10.0.0.1','KEQ0909042','4','SET_TEMPERATURE')
	#print('result: '+res)
	s=settings.settings(1)
	interface=hmInterface(s)
	#print('result: '+str(interface.update('KEQ0909042','4','ACTUAL_TEMPERATURE')))
	
	script='mySysVar=dom.GetObject("BidCos-RF.KEQ0909042:4.ACTUAL_TEMPERATURE").Value();'
	
	script=       'var objIDs = dom.GetObject(ID_ROOMS).EnumUsedIDs();\n'
	script=script+'string id;\n'
	script=script+'! Alle Datenpunkte durchlaufen\n'
	script=script+'foreach(id, objIDs){\n'
	script=script+'  ! Einzelnen Datenpunkt holen\n'
	script=script+'  var object = dom.GetObject(id);\n'
	script=script+'  ! Namen und Wert des Elements ausgeben\n'
	script=script+'  WriteLine("Name: " # object.Name() # ": " #  object.ID());\n'
	script=script+'}'
	#script='var b=2*3;'
	
	#script=g_roomsScript
	text=interface.getResultFromScript(script)
	print(text)
	
	#root = ET.fromstring(text)
	#print('')
	#print('root: '+str(root))
	#for child in root:
		#print(str(child.tag)+'    '   +  str(child.attrib))

