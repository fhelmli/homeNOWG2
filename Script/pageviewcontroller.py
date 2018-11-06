import socket
import SimpleHTTPServer
import BaseHTTPServer
import time

from hmscripts import testHMScripts
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





# test code:

numTetrisGames = 1


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
		
		if self.path=='/oachkatzlschwoaf0815':
			pass
		else:
			myServer.server_close()
			return
		self.wfile.write(bytes("<html><body>" + allCCUInfoInOne)) # + allCCUInfoInOne
		for x in range(numTetrisGames):
			self.wfile.write(bytes(
								   """
									   <h1><p>NEW TEST FOR CONTINUOUS INTEGRATION!</p>This WebView content was written in Python! Additional data sent from Python code: """ + str(x))) # % str(x))) # self.path, "utf-8"))
		
		for i in range(1000):
			self.wfile.write(bytes("""
				<h1>All content was sent to the WebView from Python code. Additional data: %s<p><p>Simple SVG file:</h1>
				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 68 65">
				<path fill="#1A374D" d="M42 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v21l12 15-7 15.7c14.5 13.9 35 2.8 35-13.7 0-13.3-13.4-21.8-26-18zm6 25c-3.9 0-7-3.1-7-7s3.1-7 7-7 7 3.1 7 7-3.1 7-7 7z"/>
				<path d="M14 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v41c0 8.2 9.2 17 20 17s20-9.2 20-20c0-13.3-13.4-21.8-26-18zm6 25c-3.9 0-7-3.1-7-7s3.1-7 7-7 7 3.1 7 7-3.1 7-7 7z"/>
				</svg>
				
				
				""" % str(i))) # self.path, "utf-8"))

		#time.sleep(2.0)
		
		#if inAnApp:
		#	myServer.server_close()


	#def log_message(self, format, *args):
		#pass


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
