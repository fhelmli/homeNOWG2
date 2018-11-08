import socket
import SimpleHTTPServer
import BaseHTTPServer
import time

from hmscripts import testHMScripts

from translation import tr, setGlobalLanguage

#import svgmanager

"""
class PageViewController:
	pages=[]
	windows=[]
	
	name=''
	interface=''
	
	def __init__(self,interface=None):
		print('hmccu constructor: ')
		self.interface=interface
	
	def updateConfig():
		print('hmccu update config: ')
		if self.interface==None:
			raise Exception('hmccu: no interface defined!')
		
		#update rooms
		#update sections
		#update devices
		
	def updateValues(self):
		print('hmccu update values: ')
		if self.interface==None:
			raise Exception('hmccu: no interface defined!')
		for element in self.devices.devices:
			element.print()
			element.update(self.interface)

	def print(self):
		print('hmccu  print: ')
		self.devices.print()
		print(self.rooms)
		print(self.sections)

"""


nextWindowId = 0
additionalContents = ""


def addWindow(additionalContents, nextWindowId = None):
	if additionalContents==None:
		additionalContents = ""

	if nextWindowId==None:
		nextWindowId = 0

	additionalContents = additionalContents + '<div id="window' + str(nextWindowId) + '" style="width:500px;height:300px;border:1px solid #000;">This is a window, number ' + str(nextWindowId) + '!</div>'
	nextWindowId = nextWindowId + 1

	return additionalContents, nextWindowId

def insertTextInWindow(index, text):
	return """/*eval*/document.getElementById('window""" + str(index) + """').innerHTML = 'Window contents of window """ + str(index) + """ changed to """ + text + """!<p>Translation test: de/en: <p>""" + tr("Rooms") + " / " + tr("Rooms", "en") + "<p>" + tr("Devices", "de") + " / " + tr("Devices", "en") + """<p><svg viewBox="0 0 560 560"><path fill="#""" + str(40+index*10) +"""20""" + str(90-index*14) + """" d="M42 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v21l12 15-7 15.7c14.5 13.9 35 2.8 35-13.7 0-13.3-13.4-21.8-26-18zm6 25c-3.9 0-7-3.1-7-7s3.1-7 7-7 7 3.1 7 7-3.1 7-7 7z"/><path d="M14 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v41c0 8.2 9.2 17 20 17s20-9.2 20-20c0-13.3-13.4-21.8-26-18zm6 25c-3.9 0-7-3.1-7-7s3.1-7 7-7 7 3.1 7 7-3.1 7-7 7z"/></svg>';"""



# test code:

hostName = ""
hostPort = 8083

# TEST! show all results of all "get all infos" HMScripts
allCCUInfoInOne = "" #testHMScripts()


BaseHTTPRequestHandler = SimpleHTTPServer.SimpleHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
	
	def end_headers (self):
		self.send_header('Access-Control-Allow-Origin', '*')
		BaseHTTPRequestHandler.end_headers(self)
	
	#	GET is for view getting data from view controller (= a HTTP server in our case)
	def do_GET(self):
		self.send_response(200, 'OK')
		self.send_header('Content-type', 'html')
		self.end_headers()
		
		if self.path=='/oachkatzlschwoaf0815' or self.path=='/oachkatzlschwoaf0815_getWindowContent':
			pass
		else:
			myServer.server_close()
			return
		
		
		# TEST
		if self.path=='/oachkatzlschwoaf0815':
			additionalContents = ""
			
			setGlobalLanguage("de")

			additionalContents += tr("Favorites")

			setGlobalLanguage("en")

			additionalContents += tr("Functions")

			setGlobalLanguage("en")

			additionalContents += tr("Password")

			setGlobalLanguage("de")

			additionalContents += tr("Rooms")


			winId = None
			additionalContents, winId = addWindow(additionalContents, winId)
			additionalContents, winId = addWindow(additionalContents, winId)
			additionalContents, winId = addWindow(additionalContents, winId)
			additionalContents, winId = addWindow(additionalContents, winId)
			additionalContents, winId = addWindow(additionalContents, winId)
			
			windows = "<h1>Windows test:</h1><p>" + additionalContents
		

			self.wfile.write(bytes("<html><body>" + windows)) # + allCCUInfoInOne
		if self.path=='/oachkatzlschwoaf0815_getWindowContent':
			contentsInWindows = insertTextInWindow(0, "COOL0")
			contentsInWindows += insertTextInWindow(1, "COOL1")
			contentsInWindows += insertTextInWindow(2, "COOL2")
			contentsInWindows += insertTextInWindow(3, "COOL3")
			contentsInWindows += insertTextInWindow(4, "COOL4")
			self.wfile.write(bytes(contentsInWindows))

		
		#if inAnApp:
		#	myServer.server_close()


	def log_message(self, format, *args):
		pass


myServer = BaseHTTPServer.HTTPServer((hostName, hostPort), MyServer)

#print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))


def worker(q):
	try:
		myServer.serve_forever()
	#except KeyboardInterrupt:
	#	pass
	except:
		pass
	
	myServer.server_close()
#print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))


"""
def test():
	print('hmccu  test: ')
	myhmccu=hmCCU()
	mydevices=hmdevices.hmDevices()
	mydev=hmdevice.hmDevice()
	mydevices.add(mydev)
	myhmccu.devices=mydevices
	myhmccu.print()
	
#test()
"""
