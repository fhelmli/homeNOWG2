import logging
import xml.etree.ElementTree as ET		
import urllib.request
import base64

import settings


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




class hmInterface:
	url=''
	def __init__(self,url):
		print("hminterface constructor")
		self.url=url
		#test interface
	
	def getResultFromScript(self,script):
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
	
	def updateId(self,id):
		print ('hm interface updateid id: '+str(id))
		script='mySysVar=dom.GetObject(' + str(id) + ').Value();'
		val=self.getResultFromScript(script)
		res = find_between(str(val), '<mySysVar>', '</mySysVar>')
		return res
	
	def update(self,serial,port,key):
		val=getValue(self.url,serial,port,key)
		return val
	
	def generateDeviceList(self):
		print('hminterface generate device list')
	
	
	
	def print(self):
		print('hminterface print:')




def test():
	print('hminterface test: ')
	#res=getValue('10.0.0.1','KEQ0909042','4','SET_TEMPERATURE')
	#print('result: '+res)
	s=settings.settings(2)
	interface=hmInterface(s.url())
	print('result: '+str(interface.update('KEQ0909042','4','ACTUAL_TEMPERATURE')))
	
	script='mySysVar=dom.GetObject("BidCos-RF.KEQ0909042:4.ACTUAL_TEMPERATURE").Value();'
	
	text=interface.getResultFromScript(script)
	print(text)
	root = ET.fromstring(text)
	print('')
	print('root: '+str(root))
	for child in root:
		print(str(child.tag)+'    '   +  str(child.attrib))
	
#test()
