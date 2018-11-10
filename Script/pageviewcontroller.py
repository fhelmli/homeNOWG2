# -*- coding: utf-8

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
		
		if '/oachkatzlschwoaf0815_' in self.path or ('/oachkatzlschwoaf0815_' in self.path and '_getWindowContent' in self.path):
			pass
		else:
			myServer.server_close()
			return
		
		
		# TEST
		if '/oachkatzlschwoaf0815_' in self.path and not '_getWindowContent' in self.path:
			additionalContents = ""
			
			setGlobalLanguage("de")

			additionalContents += " " + tr("Favorites")

			setGlobalLanguage("en")

			additionalContents += " " + tr("Functions")

			setGlobalLanguage("en")

			additionalContents += " " + tr("Password")

			setGlobalLanguage("de")

			additionalContents += " " + tr("Rooms")


			winId = None
			additionalContents, winId = addWindow(additionalContents, winId)
			additionalContents, winId = addWindow(additionalContents, winId)
			additionalContents, winId = addWindow(additionalContents, winId)
			additionalContents, winId = addWindow(additionalContents, winId)
			additionalContents, winId = addWindow(additionalContents, winId)
			
			windows = "<h1>Windows test:</h1><p>" + additionalContents
		

			self.wfile.write(bytes("""
				
				
				<!--
				Version 0.18 Robert Peiﬂl & Thomas Berk 20160415
				Bewegung und Energieverbrauch grau
				-->
				
				<div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 widget-container">
				<section class="widget">
				<form role="form">
				<fieldset>
				<svg version="1.1" x="0px" y="0px"width="100px" height="96px" viewBox="0 0 256 271" xml:space="preserve" fill="currentColor">
				<svg id="VariableElementID_1" x="0px" y="0px">
				<!--Haus-->
				<linearGradient id="VariableElementID_41" gradientUnits="userSpaceOnUse" x1="264.0225" y1="-146.52" x2="323.1574" y2="-199.8991" gradientTransform="matrix(1 0 0 -1 -169.5 -36)">
				<stop  offset="0" style="stop-color:#DEFC08"/>
				<stop  offset="1" style="stop-color:#95C11F"/>
				</linearGradient>
				<path fill="url(#VariableElementID_41)" d="M95.162,157.473c0,0-0.078,2.026,1.901,2.026c2.464,0,57.667-0.087,60.703-0.087c2.514,0,2.398-2.521,2.398-2.521v-34.526l-31.529-28.045l-33.474,28.046L95.162,157.473L95.162,157.473z"/>
				<linearGradient id="VariableElementID_42" gradientUnits="userSpaceOnUse" x1="274.3955" y1="-135.0293" x2="333.5295" y2="-188.4075" gradientTransform="matrix(1 0 0 -1 -169.5 -36)">
				<stop  offset="0" style="stop-color:#DEFC08"/>
				<stop  offset="1" style="stop-color:#95C11F"/>
				</linearGradient>
				<path fill="url(#VariableElementID_42)" d="M82.496,119.754c0,0,2.844,5.24,9.041,0l37.038-31.332l34.73,31.139c7.172,5.174,9.861,0,9.861,0L128.574,79.17L82.496,119.754z"/>
				</svg>
				<svg id="VariableElementID_0" visibility="hidden" x="0px" y="0px">
				<!--Rauch-->
				<path fill="#9D9D9C" d="M119.358,142.948c2.875,4.169,8.599,5.203,12.781,2.317c3.793-2.619,4.986-7.553,3.041-11.561c2.283-0.208,4.547-0.927,6.57-2.324c5.961-4.113,7.611-12.059,4.025-18.182c2.543-0.086,5.096-0.853,7.35-2.407c6.248-4.31,7.832-12.849,3.539-19.069c-0.553-0.804-1.182-1.522-1.865-2.167c1.537-0.486,3.041-1.127,4.434-2.089c7.514-5.185,9.42-15.453,4.258-22.935c-5.164-7.483-15.441-9.344-22.955-4.16c-1.533,1.059-2.771,2.367-3.822,3.783c-4.932-1.912-10.7-1.423-15.393,1.815c-7.512,5.184-9.417,15.453-4.255,22.935c1.188,1.723,2.667,3.106,4.297,4.216c-6.026,4.365-7.529,12.732-3.297,18.865c0.877,1.271,1.965,2.292,3.139,3.164c-1.608,4.097-1.221,8.888,1.46,12.772c0.315,0.456,0.697,0.835,1.054,1.235c-0.689,0.261-1.363,0.577-1.995,1.015C117.545,133.064,116.484,138.783,119.358,142.948z"/>
				</svg>
				<svg id="VariableElementID_2" visibility="hidden" x="0px" y="0px">
				<!--Feuchtigkeit-->
				<path fill="#1D71B8" d="M167.316,160.863l-12.09,6.697c-0.975,0.539-3.096,0.516-4.059-0.036l-7.094-4.109c-3.77-2.188-9.35-2.36-13.26-0.42l-9.381,4.658c-1.026,0.512-3.217,0.42-4.178-0.172l-6.318-3.892c-3.756-2.315-9.351-2.548-13.3-0.563l-13.682,6.869c-2.322,1.167-3.26,3.993-2.095,6.315c0.827,1.645,2.485,2.594,4.208,2.594c0.711,0,1.431-0.162,2.108-0.499l13.684-6.87c1.017-0.511,3.187-0.425,4.144,0.162l6.319,3.893c3.748,2.31,9.335,2.554,13.295,0.592l9.381-4.658c1.059-0.527,3.342-0.463,4.361,0.132l7.094,4.109c3.842,2.226,9.449,2.279,13.33,0.124l12.09-6.695c2.273-1.257,3.098-4.12,1.834-6.392C172.453,160.426,169.59,159.598,167.316,160.863z"/>
				</svg>
				<svg id="VariableElementID_3" visibility="hidden" x="0px" y="0px">
				<!--Wasser-->
				<path fill="#1D71B8" d="M167.316,145.184l-12.09,6.697c-0.975,0.54-3.096,0.519-4.059-0.037l-7.094-4.109c-3.77-2.188-9.35-2.359-13.26-0.419l-9.381,4.658c-1.026,0.513-3.217,0.42-4.178-0.172l-6.318-3.894c-3.756-2.314-9.351-2.546-13.3-0.562l-13.682,6.87c-2.322,1.167-3.26,3.993-2.095,6.314c0.827,1.645,2.485,2.592,4.208,2.592c0.711,0,1.431-0.16,2.108-0.497l13.684-6.87c1.017-0.513,3.187-0.424,4.144,0.163l6.319,3.892c3.748,2.311,9.335,2.558,13.295,0.591l9.381-4.657c1.059-0.525,3.342-0.463,4.361,0.131l7.094,4.109c3.842,2.227,9.449,2.275,13.33,0.123l12.09-6.693c2.273-1.258,3.098-4.12,1.834-6.392C172.453,144.746,169.59,143.921,167.316,145.184z"/>
				<path fill="#1D71B8" d="M81.908,144.823c0.809,1.656,2.453,2.618,4.16,2.618c0.691,0,1.394-0.159,2.055-0.49l13.684-6.867c0.464-0.234,1.16-0.345,1.876-0.345c0.901,0,1.833,0.179,2.379,0.513l6.318,3.896c2.039,1.256,4.629,1.896,7.2,1.896c2.112,0,4.212-0.433,5.981-1.311l9.381-4.658c0.496-0.246,1.252-0.368,2.025-0.368c0.928,0,1.879,0.172,2.449,0.5l7.092,4.112c1.945,1.125,4.344,1.69,6.742,1.69c2.297,0,4.594-0.521,6.477-1.567l12.09-6.697c2.248-1.242,3.074-4.101,1.85-6.381c-0.842-1.563-2.436-2.45-4.076-2.45c-0.75,0-1.512,0.187-2.217,0.577l-5.158,2.856l-1.725,0.953l-5.207,2.884c-0.488,0.272-1.254,0.405-2.029,0.405c-0.812,0-1.635-0.147-2.143-0.44l-1.619-0.938l-5.475-3.173c-1.629-0.942-3.598-1.489-5.621-1.668c-0.469-0.041-0.936-0.085-1.406-0.085c-0.055,0-0.107,0.01-0.162,0.01c-0.525,0.004-1.049,0.034-1.568,0.092c-1.564,0.173-3.076,0.581-4.395,1.234l-3.727,1.853l-3.157,1.568l-0.339,0.168l-2.159,1.072c-0.43,0.211-1.061,0.312-1.72,0.327c-0.053,0.002-0.103,0.013-0.157,0.013c-0.088,0-0.174-0.009-0.262-0.013c-0.418-0.016-0.83-0.066-1.204-0.153c-0.365-0.086-0.697-0.202-0.945-0.352l-1.45-0.895l-4.867-3c-2.034-1.251-4.613-1.889-7.174-1.889c-2.126,0-4.238,0.439-6.016,1.331l-3.218,1.616l-1.402,0.704l-1.394,0.698l-7.668,3.85C81.71,139.671,80.77,142.493,81.908,144.823z"/>
				</svg>
				<svg fill="#999999" x="0px" y="0px">
				<!--Gl¸hbirne-->
				<path d="M188.473,43.657c0,0.565-0.456,1.023-1.022,1.023h-10.228c-0.565,0-1.022-0.458-1.022-1.023c0-0.565,0.457-1.022,1.022-1.022h10.228C188.017,42.634,188.473,43.092,188.473,43.657z"/>
				<path d="M187.45,45.702h-10.228c-0.565,0-1.022,0.458-1.022,1.022c0,0.565,0.457,1.023,1.022,1.023h10.228c0.566,0,1.022-0.458,1.022-1.023C188.473,46.16,188.017,45.702,187.45,45.702z"/>
				<path d="M180.291,50.816h4.092c1.13,0,2.045-0.915,2.045-2.045h-8.183C178.245,49.901,179.16,50.816,180.291,50.816z"/>
				<path id="VariableElementID_4" d="M192.563,28.316c0,5.561-3.352,6.208-3.981,12.272c0,0.565-0.456,1.023-1.022,1.023h-10.446c-0.565,0-1.022-0.458-1.022-1.023h-0.003c-0.627-6.064-3.979-6.711-3.979-12.272c0-5.649,4.579-10.228,10.228-10.228S192.563,22.667,192.563,28.316z"/>
				</svg>
				<svg id="VariableElementID_5" visibility="visible" fill="#999999" x="0px" y="0px">
				<!--Fenster zu-->
				<path d="M210.825,128.145v14.301c0,0.224,0.097,0.437,0.264,0.584c0.143,0.124,0.326,0.193,0.514,0.193c0.032,0,0.065-0.004,0.099-0.007l14.723,0.007c0.387-0.05,0.777-0.387,0.777-0.777v-14.301c0-0.428-0.348-0.777-0.775-0.777h-14.825C211.172,127.368,210.825,127.717,210.825,128.145z M212.377,128.92h13.271v12.643h-13.271V128.92z M228.247,128.145v14.301c0,0.224,0.097,0.437,0.266,0.584c0.142,0.124,0.324,0.193,0.512,0.193c0.033,0,0.066-0.004,0.1-0.007l14.722,0.007c0.387-0.05,0.777-0.387,0.777-0.777v-14.301c0-0.428-0.347-0.777-0.775-0.777h-14.825C228.595,127.368,228.247,127.717,228.247,128.145z M229.8,128.92h13.271v12.643H229.8V128.92z M210.825,111.243v14.301c0,0.223,0.097,0.437,0.264,0.584c0.143,0.124,0.326,0.193,0.514,0.193c0.032,0,0.065-0.004,0.099-0.007l14.723,0.007c0.387-0.05,0.777-0.387,0.777-0.777v-14.301c0-0.428-0.348-0.777-0.775-0.777h-14.825C211.172,110.465,210.825,110.814,210.825,111.243z M212.377,112.017h13.271v12.645h-13.271V112.017z M228.247,111.243v14.301c0,0.223,0.097,0.437,0.266,0.584c0.142,0.124,0.324,0.193,0.512,0.193c0.033,0,0.066-0.004,0.1-0.007l14.722,0.007c0.387-0.05,0.777-0.387,0.777-0.777v-14.301c0-0.428-0.347-0.777-0.775-0.777h-14.825C228.595,110.465,228.247,110.814,228.247,111.243z M229.8,112.017h13.271v12.645H229.8V112.017z"/>
				</svg>
				<svg id="VariableElementID_6" visibility="hidden" x="0px" y="0px">
				<!--Fenster gekippt-->
				<path fill="#f39c12" d="M228.342,126.941v15.365c0,0.506,0.412,0.917,0.918,0.917h12.291c0.461,0,0.852-0.343,0.91-0.799l2.004-15.364c0.006-0.04,0.008-0.079,0.008-0.119c0-0.221-0.08-0.436-0.229-0.605c-0.174-0.197-0.426-0.312-0.688-0.312H229.26C228.754,126.024,228.342,126.436,228.342,126.941z M242.512,127.859l-1.766,13.529h-10.57v-13.529H242.512L242.512,127.859zM208.596,106.362c-0.174,0.198-0.252,0.462-0.219,0.724l2.203,16.901c0.061,0.457,0.449,0.8,0.91,0.8h14.697c0.506,0,0.916-0.412,0.916-0.918v-16.902c0-0.506-0.41-0.916-0.916-0.916h-16.902C209.021,106.051,208.771,106.164,208.596,106.362z M225.27,107.885v15.067h-12.975l-1.965-15.067H225.27z M210.98,127.061l2.004,15.364c0.061,0.456,0.449,0.799,0.91,0.799h12.293c0.506,0,0.916-0.411,0.916-0.917v-15.365c0-0.506-0.41-0.917-0.916-0.917h-14.297c-0.264,0-0.516,0.114-0.689,0.312C211.027,126.535,210.947,126.799,210.98,127.061zM225.27,127.859v13.529h-10.57l-1.764-13.529H225.27L225.27,127.859z M228.342,106.967v16.902c0,0.506,0.412,0.918,0.918,0.918h14.697c0.461,0,0.85-0.343,0.908-0.8l2.205-16.901c0.004-0.039,0.008-0.078,0.008-0.117c0-0.222-0.082-0.438-0.229-0.605c-0.174-0.198-0.426-0.312-0.689-0.312h-16.9C228.754,106.051,228.342,106.461,228.342,106.967z M245.117,107.885l-1.967,15.066h-12.975v-15.066H245.117z"/>
				</svg>
				<svg id="VariableElementID_7" visibility="hidden" x="0px" y="0px">
				<!--Fenster offen-->
				<path fill="#E30613" d="M227.084,127.463h-15.365c-0.506,0-0.917,0.411-0.917,0.917v12.292c0,0.461,0.343,0.852,0.799,0.91l15.364,2.004c0.04,0.006,0.079,0.008,0.119,0.008c0.221,0,0.436-0.08,0.605-0.229c0.197-0.174,0.312-0.426,0.312-0.688V128.38C228.001,127.875,227.59,127.463,227.084,127.463z M226.166,141.633l-13.529-1.766v-10.57h13.529V141.633L226.166,141.633zM247.663,107.717c-0.198-0.174-0.462-0.253-0.724-0.22l-16.901,2.204c-0.457,0.06-0.8,0.448-0.8,0.909v14.697c0,0.506,0.412,0.917,0.918,0.917h16.902c0.506,0,0.916-0.411,0.916-0.917v-16.901C247.975,108.143,247.861,107.892,247.663,107.717z M246.141,124.391h-15.067v-12.975l15.067-1.966V124.391z M226.965,110.102l-15.364,2.004c-0.456,0.06-0.799,0.449-0.799,0.91v12.292c0,0.506,0.411,0.917,0.917,0.917h15.365c0.506,0,0.917-0.411,0.917-0.917v-14.296c0-0.265-0.114-0.516-0.312-0.69C227.49,110.149,227.227,110.068,226.965,110.102zM226.166,124.391h-13.529v-10.57l13.529-1.765V124.391L226.166,124.391z M247.059,127.463h-16.902c-0.506,0-0.918,0.411-0.918,0.917v14.698c0,0.461,0.343,0.85,0.8,0.908l16.901,2.205c0.039,0.004,0.078,0.008,0.117,0.008c0.222,0,0.438-0.082,0.605-0.229c0.198-0.174,0.312-0.426,0.312-0.689V128.38C247.975,127.875,247.564,127.463,247.059,127.463zM246.141,144.238l-15.066-1.967v-12.975h15.066V144.238z"/>
				</svg>
				<svg>
				<path id="VariableElementID_8" fill="#999999" stroke="#999999" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="M179.826,237.907c-0.774-0.071-1.559-0.208-2.275-0.423c-3.512-1.048-6.534-4.117-7.286-7.733c-0.198-0.952-0.265-2.022-0.159-2.991c0.295-2.731,1.596-5.568,3.008-7.896c1.939-3.199,3.922-6.417,5.219-9.941c0.374-1.015,0.688-2.051,0.92-3.106c0.361-1.649,0.699-3.799-0.607-5.145c2.645,2.723,4.944,5.77,6.944,8.992c0.724,1.166,1.407,2.355,2.057,3.564c0.673,1.253,1.304,2.528,1.89,3.823c0.787,1.737,1.431,3.542,1.883,5.396c0.838,3.426,1.752,7.769-0.532,10.845c-1.021,1.374-2.325,2.496-3.877,3.23c-1.851,0.876-3.966,1.459-6.022,1.442C180.607,237.961,180.219,237.942,179.826,237.907z"/>
				<path id="VariableElementID_81" fill="#bbbbbb" stroke="#bbbbbb" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="M181.167,221.162c-0.723,1.744-2.265,3.15-3.208,4.788c-1.062,1.844-2.135,4.137-1.682,6.322c0.336,1.611,1.683,2.979,3.247,3.446c0.319,0.095,0.669,0.156,1.015,0.188c0.174,0.017,0.348,0.024,0.516,0.026c0.917,0.007,1.859-0.253,2.684-0.643c0.691-0.328,1.273-0.828,1.729-1.44c1.375-1.851,0.574-4.341-0.218-6.256c-1.103-2.665-2.709-5.11-4.004-7.685C181.422,220.261,181.359,220.696,181.167,221.162z"/>
				</svg>
				<svg id="VariableElementID_9" fill="#999999" x="0px" y="0px">
				<!--Laubblatt-->
				<path d="M64.774,208.906c-8.194,4.754-7.724,12.5-7.442,15.365c10.584-12.538,26.417-11.93,26.417-11.93s-22.442,7.697-29.034,23.135c-0.521,1.219,2.442,2.804,3.118,1.363c2.019-4.294,4.831-7.514,4.831-7.514c4.149,1.545,11.327,3.354,16.415-0.227c6.758-4.756,6.067-15.298,15.714-20.431C97.046,207.471,75.883,202.459,64.774,208.906z"/>
				</svg>
				<svg id="VariableElementID_10" x="0px" y="0px">
				<!--Person-->
				<!--path fill="#999999" d="M21.833,109c4.909,0,7.013,2.805,6.305,8.694c0.633,0.362,1.059,1.044,1.059,1.826c0,0.957-0.638,1.764-1.512,2.02c-0.364,1.301-0.931,2.452-1.644,3.374v4.426c2.337,0.468,4.208,0.701,7.013,2.104c2.807,1.401,3.741,2.688,5.611,4.558v6.663H5.001v-6.663c1.871-1.87,2.805-3.156,5.611-4.558c2.805-1.403,4.676-1.637,7.013-2.104v-4.426c-0.712-0.921-1.279-2.073-1.644-3.374c-0.874-0.256-1.512-1.063-1.512-2.02c0-0.782,0.426-1.464,1.059-1.826C14.82,111.805,16.924,109,21.833,109z"/>
				<!--Person-->
				<circle id="VariableElementID_101" fill="#999999" cx="20.977" cy="108.65" r="4.181"/>
				<!--Bein in Bewegung-->
				<path id="VariableElementID_102" visibility="hidden" fill="#f39c12" d="M12.958,141.554c-0.661,1.129-0.625,2.521,0.507,3.355c0.969,0.715,2.694,0.622,3.356-0.506c1.369-2.337,3.851-4.095,3.851-4.095s-0.912-2.013-1.347-5.787C19.325,134.521,14.516,138.897,12.958,141.554z"/>
				<!--Kˆrber in Bewegung-->
				<path id="VariableElementID_103" visibility="hidden" fill="#f39c12" d="M32.488,121.242c-2.811-2.501-5.823-4.744-9.123-6.549c-0.354-0.268-0.76-0.478-1.189-0.62c-0.285-0.115-0.567-0.172-0.839-0.18c-0.453-0.051-0.906-0.028-1.321,0.083c-1.096,0.294-1.836,0.964-2.258,1.817c-2.032,2.374-3.729,4.954-5.252,7.679c-1.514,2.704,2.632,5.124,4.144,2.422c0.473-0.846,0.959-1.679,1.468-2.497c0.438,2.954,0.875,5.908,1.312,8.861c0.089,0.599,0.374,1.115,0.772,1.535c0.637,4.204,1.804,8.354,3.648,12.169c1.343,2.787,5.48,0.352,4.143-2.421c-1.377-2.852-2.297-6.007-2.865-9.192c1.247-0.868,1.697-2.43,1.465-4.009c-0.434-2.918-0.865-5.835-1.298-8.753c1.313,0.947,2.577,1.962,3.799,3.047C31.402,126.684,34.808,123.303,32.488,121.242z"/>
				<!--keine Bewegung-->
				<path id="VariableElementID_104" fill="#999999" d="M31.537,127.354c-0.966-10.844-6.133-13.006-6.133-13.006s-4.995-3.003-10.252,0.822c-3.408,3.101-4.195,7.838-4.735,12.412c-0.271,2.326,3.365,2.297,3.634,0c0.322-2.729,0.781-5.472,2.135-7.807l-0.005,2.634l-0.026,12.664v10.048c0,1.083,0.792,1.957,1.905,1.957c1.11,0,2.012-0.874,2.012-1.957v-14.361h1.779c0,3.365,0,11.045,0,14.407c0,2.345,3.631,2.345,3.631,0c0-3.364,0-6.729,0-10.094l0.155-12.69c0-1.211,0.002-2.293,0.002-3.046c1.453,2.379,1.933,5.203,2.264,8.016C28.175,129.649,31.81,129.678,31.537,127.354z"/>
				</svg>
				<svg id="VariableElementID_11" x="0px" y="0px" fill="#999999">
				<!--Vorh‰ngeSchloﬂ-->
				<svg id="VariableElementID_12" x="0px" y="0px">
				<path d="M83.841,32.986V28.59c0-2.809-1.008-5.22-3.021-7.234c-2.016-2.016-4.426-3.022-7.234-3.022c-2.808,0-5.221,1.007-7.234,3.022c-2.016,2.015-3.022,4.426-3.022,7.234v4.396 M67.723,32.987 M79.446,32.987L79.446,32.987M67.723,32.987v-4.396c0-1.618,0.573-3,1.718-4.145s2.526-1.717,4.144-1.717s2.999,0.572,4.145,1.717s1.717,2.526,1.717,4.145v4.396 M63.329,32.986l4.394,0.001 M79.446,32.987l4.395-0.001"/>
				</svg>
				<path d="M63.328,32.818h-0.732c-0.61,0-1.129,0.214-1.557,0.641c-0.428,0.428-0.642,0.946-0.642,1.558v13.188c0,0.609,0.214,1.129,0.642,1.557c0.428,0.428,0.946,0.641,1.557,0.641h21.979c0.61,0,1.13-0.213,1.558-0.641s0.641-0.945,0.641-1.557V35.018c-0.002-0.61-0.217-1.13-0.645-1.558c-0.428-0.427-0.945-0.641-1.557-0.641H83.84 M63.328,32.818H83.84"/>
				</svg>
				<svg x="0px" y="0px">
				<!--Strom-Verbrauchs-Wert-->
				<text x="105" y="225">
				<tspan id="VariableElementID_13" fill="currentColor" text-anchor="end" font-size="20"></tspan>
				</text>
				</svg>
				<svg id="VariableElementID_14" visibility="hidden" x="0px" y="0px" fill="#7F7F7F">
				<!--Batterie-Symbol-->
				<path fill="#4FC2EB" d="M120.155,117.866c-0.429-0.438-0.96-0.664-1.586-0.664H91.754c-0.609,0-1.125,0.221-1.568,0.664c-0.442,0.442-0.663,0.958-0.663,1.568v3.024h-1.734c-0.571,0-1.015,0.442-1.015,1.014v0.074v0.111v4.426v0.073v0.111c0,0.571,0.443,1.014,1.015,1.014h1.734v2.951c0,0.608,0.221,1.125,0.663,1.568c0.443,0.442,0.959,0.663,1.568,0.663h26.815c0.626,0,1.166-0.217,1.586-0.646c0.429-0.438,0.646-0.978,0.646-1.586v-12.799C120.801,118.824,120.574,118.294,120.155,117.866zM118.753,132.232c0,0.129-0.055,0.185-0.184,0.185H91.754c-0.074,0-0.185-0.11-0.185-0.185v-12.799c0-0.074,0.11-0.185,0.185-0.185h26.815c0.129,0,0.185,0.055,0.185,0.185L118.753,132.232L118.753,132.232z"/>
				<rect x="109.92" y="120.798" fill="#4FC2EB" width="7.1" height="10.069"/>
				</svg>
				<svg id="VariableElementID_15" visibility="hidden" x="0px" y="0px" fill="#7F7F7F">
				<!--Antennen-Symbol-->
				<path fill="#534093" d="M135.848,119.778c0,3.603,1.404,6.991,3.956,9.54l-2.201,2.201c-3.139-3.138-4.867-7.307-4.867-11.741c0-4.433,1.727-8.604,4.863-11.736l2.2,2.2C137.25,112.788,135.848,116.175,135.848,119.778z M144.565,115.008l-2.201-2.2c-1.86,1.864-2.886,4.34-2.886,6.97c0,2.635,1.025,5.111,2.89,6.971l2.201-2.2c-1.276-1.273-1.979-2.967-1.979-4.771C142.591,117.979,143.293,116.285,144.565,115.008z M161.067,108.038l-2.201,2.201c2.552,2.549,3.956,5.938,3.956,9.54c0,3.603-1.402,6.991-3.949,9.54l2.2,2.201c3.135-3.138,4.861-7.307,4.861-11.741C165.935,115.341,164.206,111.171,161.067,108.038zM149.335,116.666c-1.718,0-3.112,1.394-3.112,3.112c0,1.151,0.63,2.144,1.556,2.681v18.778h3.112v-18.776c0.927-0.539,1.557-1.532,1.557-2.683C152.447,118.06,151.056,116.666,149.335,116.666z M156.302,112.808l-2.201,2.2c1.274,1.277,1.979,2.971,1.979,4.77c0,1.804-0.702,3.498-1.975,4.771l2.201,2.2c1.86-1.86,2.886-4.336,2.886-6.971C159.191,117.145,158.166,114.672,156.302,112.808z"/>
				</svg>
				</svg>
				<div style="position:absolute; top:50px;" hidden>
				<span id="VariableTextID_0">RauchmelderGruppe</span>
				<span id="VariableTextID_2">WassermelderGruppe</span>
				<span id="VariableTextID_3">LichtGruppe</span>
				<span id="VariableTextID_4">FensterGruppe</span>
				<span id="VariableTextID_5">HeizungsGruppe</span>
				<span id="VariableTextID_6">EnergieGruppe</span>
				<span id="VariableTextID_7">AnwesendGruppe</span>
				<span id="VariableTextID_8">SicherheitsGruppe</span>
				</div>
				</fieldset>
				</form>
				</section>
				</div>
				
				<script>
				
				OnChanged_VariableTextID_0 = function ()
				{ var Rauchmelder = $("#VariableTextID_0").html();
				
				if (Rauchmelder=="true") { $("#VariableElementID_0").attr("visibility", "visible");}
				else { $("#VariableElementID_0").attr("visibility", "hidden");}
				};
				
				OnChanged_VariableTextID_2 = function ()
				{ var Wassermelder = $("#VariableTextID_2").html();
				
				if (Wassermelder==1) { $("#VariableElementID_2").attr("visibility", "visible"); $("#VariableElementID_3").attr("visibility", "hidden");}
				else if (Wassermelder==2) { $("#VariableElementID_2").attr("visibility", "visible"); $("#VariableElementID_3").attr("visibility", "visible");}
				else { $("#VariableElementID_2").attr("visibility", "hidden"); $("#VariableElementID_3").attr("visibility", "hidden");}
				};
				
				OnChanged_VariableTextID_3 = function ()
				{ var Licht = $("#VariableTextID_3").html();
				
				if (Licht=="true") { $("#VariableElementID_4").attr("fill", fill="#FFED00");}
				else { $("#VariableElementID_4").attr("fill", fill="#999999");}
				};
				
				
				OnChanged_VariableTextID_4 = function ()
				{ var Fenster = $("#VariableTextID_4").html();
				
				if (Fenster==0) { $("#VariableElementID_5").attr("visibility", "visible"); $("#VariableElementID_5").attr("fill", "#95C11F"); $("#VariableElementID_6").attr("visibility", "hidden"); $("#VariableElementID_7").attr("visibility", "hidden");}
				else if (Fenster==1) { $("#VariableElementID_5").attr("visibility", "hidden"); $("#VariableElementID_6").attr("visibility", "visible"); $("#VariableElementID_7").attr("visibility", "hidden");}
				else if (Fenster==2) { $("#VariableElementID_5").attr("visibility", "hidden"); $("#VariableElementID_6").attr("visibility", "hidden"); $("#VariableElementID_7").attr("visibility", "visible");}
				else { $("#VariableElementID_5").attr("visibility", "visible"); $("#VariableElementID_5").attr("fill", "#999999"); $("#VariableElementID_6").attr("visibility", "hidden"); $("#VariableElementID_7").attr("visibility", "hidden");}
				};
				
				OnChanged_VariableTextID_5 = function ()
				{ var Heizung = $("#VariableTextID_5").html();
				
				if (Heizung=="true") {$("#VariableElementID_8").attr("stroke","#f39c12");$("#VariableElementID_81").attr("stroke","#FFED00");$("#VariableElementID_8").attr("fill","#f39c12");$("#VariableElementID_81").attr("fill","#FFED00");}
				else {$("#VariableElementID_8").attr("stroke","#999999");$("#VariableElementID_81").attr("stroke","#bbbbbb");$("#VariableElementID_8").attr("fill","#999999");$("#VariableElementID_81").attr("fill","#bbbbbb");}
				};
				
				OnChanged_VariableTextID_6 = function ()
				{ var Energieverbrauch = $("#VariableTextID_6").html();
				
				if (Energieverbrauch>0) {
				$("#VariableElementID_9").attr("fill", "#95C11F");
				Energieverbrauch = Math.round(parseFloat(Energieverbrauch)) + " W";
				$("#VariableElementID_13").text(Energieverbrauch);}
				
				else {$("#VariableElementID_9").attr("fill", "#999999");
				$("#VariableElementID_13").text("");}
				
				};
				
				OnChanged_VariableTextID_7 = function ()
				{ var movement = $("#VariableTextID_7").html();
				
				if (movement=="true"){
				$("#VariableElementID_104").attr("visibility", "hidden");
				$("#VariableElementID_101").attr("fill", "#f39c12");
				$("#VariableElementID_102").attr("visibility", "visible");
				$("#VariableElementID_103").attr("visibility", "visible");
				}
				else{
				$("#VariableElementID_104").attr("visibility", "visible");
				$("#VariableElementID_101").attr("fill", "#999999");
				$("#VariableElementID_102").attr("visibility", "hidden");
				$("#VariableElementID_103").attr("visibility", "hidden");
				//$("#VariableElementID_104").attr("fill", "#95C11F");
				}
				};
				
				OnChanged_VariableTextID_8 = function ()
				{ var Sicherheit = $("#VariableTextID_8").html();
				
				var color = "#7F7F7F";
				var Xmove = "0";
				
				if (Sicherheit==0) { color = "#95C11F"; Xmove = "15";}
				else if (Sicherheit==1) { color = "#f39c12"; Xmove = "0";}
				else if (Sicherheit==2) { color = "#E30613"; Xmove = "0";}
				else { color = "#7F7F7F";}
				
				$("#VariableElementID_11").attr("fill", color);
				$("#VariableElementID_12").attr("x", Xmove);
				
				};
				
				</script>

				
				
				""" + """
					<div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 widget-container">
					<section class="widget">
					<form role="form">
					<fieldset>

					
					""" + windows + """
						</fieldset>
						</form>
						</section>
						</div>

						
						""")) # + allCCUInfoInOne
		if '/oachkatzlschwoaf0815_' in self.path and '_getWindowContent' in self.path:
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
