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


def executeHMScript(url, script):
    hmScript = script
    
    username = 'admin'
    password = 'cool2piktm'
    url = "http://10.0.0.2:8181/Test.exe"

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





g_roomsScript = "var x = 42;\n"+\
"object  oRoom;\n"+\
"string  sRoomId;\n"+\
"string  sChannelId;\n"+\
"boolean bFirst       = true;\n"+\
"boolean bFirstSecond = true;\n"+\
"\n"+\
"Write('{');\n"+\
"foreach (sRoomId, dom.GetObject(ID_ROOMS).EnumUsedIDs())\n"+\
"{\n"+\
"    if (bFirst == false) {\n"+\
"      WriteLine(',');\n"+\
"    } else {\n"+\
"      bFirst = false;\n"+\
"    }\n"+\
"    oRoom = dom.GetObject(sRoomId);\n"+\
"	Write('\"' # sRoomId # '\": ');\n"+\
"    Write('{\"Name\": \"');\n"+\
"    WriteURL(oRoom.Name());\n"+\
"    Write('\", \"TypeName\":\"' # oRoom.TypeName() # '_ROOMS');\n"+\
"    Write('\", \"EnumInfo\":\"');\n"+\
"    WriteURL(oRoom.EnumInfo());\n"+\
"    Write('\", \"Channels\":[');\n"+\
"	bFirstSecond = true;\n"+\
"    foreach(sChannelId, oRoom.EnumUsedIDs()) {\n"+\
"		if (bFirstSecond == false) {\n"+\
"		  Write(',');\n"+\
"		} else {\n"+\
"		  bFirstSecond = false;\n"+\
"		}\n"+\
"		Write(sChannelId);\n"+\
"    }\n"+\
"    Write(']}');\n"+\
"}\n"+\
"WriteLine('}');";




class hmInterface:
	url=''
	demo=0
	def __init__(self,url,demo=0):
		print("hminterface constructor")
		self.demo=demo
		self.url=url
		#test interface
	
	def getResultFromScript(self,script):
		if self.demo==1:
			return random.randrange(10,40)
		return executeHMScript(self.url,script)
		
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
		
		print ('hm interface updateid id: '+str(id))
		if self.demo==1:
			return random.randrange(10,40)
		script='mySysVar=dom.GetObject(' + str(id) + ').' + what + '();'
		val=self.getResultFromScript(script)
		res = find_between(str(val), '<mySysVar>', '</mySysVar>')
		return res
	
	def update(self,serial,port,key,what='Value'):
		print ('hm interface updateid normal: '+str(serial)+' '+str(port)+' '+str(key))
		if self.demo==1:
			return random.randrange(10,40)
		script = 'mySysVar=dom.GetObject("BidCos-RF.'
		script = script + serial + ':' +  port + '.' +  key +'"'
		script = script + ').' + what + '();'
		
		val=self.getResultFromScript(script)
		print ('val: '+ str(val))
		res = find_between(str(val), '<mySysVar>', '</mySysVar>')
		return res

	def generateDeviceList(self):
		print('hminterface generate device list')
	
	def printc(self):
		print('hminterface print:')





def test():
	print('hminterface test: ')
	#res=getValue('10.0.0.1','KEQ0909042','4','SET_TEMPERATURE')
	#print('result: '+res)
	s=settings.settings(1)
	interface=hmInterface(s.url())
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
	
#test()
