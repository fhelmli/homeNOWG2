#!/usr/bin/env python2

import imp
try:
    imp.find_module('ui')
    found = True
except ImportError:
    found = False

################################
inAnApp = False
if found:
    inAnApp = True
################################

if inAnApp:
	import ui
import os
import sys
import threading

if inAnApp:
	from objc_util import *


import SimpleHTTPServer
import SocketServer



from pageviewcontroller import worker


#######################################################
# our new bundle ID for iOS App: at.homenow.homenow2
#######################################################


	
if inAnApp:
	# iOS App:
	t = threading.Thread(target=worker, args=(0,))
	t.daemon = True
	t.start()
	
	#time.sleep(1.0)
	
	file_path = os.path.dirname(sys.executable) + '/Script/html/design0/index.html'
	if "Pythonista3" in file_path:
		file_path = os.path.abspath('html/design0/index.html')
	else:
		f = ObjCClass('NSBundle').mainBundle().bundlePath().UTF8String()
		#print f + "\n\n"
		
		#docpath = str(f.URLsForDirectory_inDomains_(9,1)[0].path())
		docpath = f
		
		file_path = docpath + '/Script/html/design0/index.html'
	
	#print file_path
	
	#print os.path.realpath(__file__)

#	directory = os.path.abspath(docpath)

#	for filename in os.listdir(directory):
#		#if filename.endswith('.html'):
#		fname = os.path.join(directory,filename)
#		print os.path.abspath(fname)




	v = ui.load_view()
	v.flex = "WH"
	
	v['webview1'].frame = 0, -44, v.width, v.height+44
	v['webview1'].flex = "WH"
	
	#v['webview1'].load_url('http://localhost:' + str(hostPort) + '/oachkatzlschwoaf0815')
	
#v['webview1'].load_url('file://' + file_path)
	
	v['webview1'].load_url(os.path.abspath(file_path))

	v.present(style='full_screen', title_bar_color='#000000',
	#hide_close_button=True,
	hide_title_bar=True,
	animated=False)
	#orientations=['portrait'])

else:
	# Android:
	#t = threading.Thread(target=worker, args=(0,))
	#t.daemon = True
	#t.start()
	
	#PORT = 5000

	#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	#Handler.extensions_map.update({
	#						  '.webapp': 'application/x-web-app-manifest+json',
	#					  });

	#httpd = SocketServer.TCPServer(("", PORT), Handler)

	##print "Serving at port", PORT
	#httpd.serve_forever()
	
	# Linux/Mac/Windows:
	worker(0)


# HTML zu Python: (User-Events, Seite geladen): Ajax zum HTTP-Server

# Python zu HTML: Ajax in Dauerschleife, wenn Jacascript-Antwort von Python kommt: dieses ausfuehren

# events von SVGs und buttons etc. zu Python, und z.B. redrawWidget, redrawWindow, redrawPage-events ueber Ajax u Python

#Editier-stuff: native UI-Elemente mit der Portablen LIb fuer Kivy und Pythonista ueber dem WebView einblenden

#Translation-File in Python, das alles auch im HTML und SVG uebersetzt, HTML und SVG muessen Englisch sein

# build apk newest test: p4a apk --private /Users/tberk/Documents/PythonistaApp/Script/ --package=org.example.myapp --name "My WebView Application" --version 0.1 --bootstrap=webview-python2 --port=5000 --sdk-dir /Users/tberk/Library/Android/sdk/ --ndk-dir /Users/tberk/Library/Android/android-ndk-r16b/ --android-api 24 --arch=armeabi-v7a --ndk-version=r16b --requirements=python2

#p4a apk --private /Users/tberk/Documents/PythonistaApp/Script/ --package=at.homenow.hn2 --name "homeNOW2" --version 0.2 --bootstrap=webview-python2 --port=5000 --sdk-dir /Users/tberk/Library/Android/sdk/ --ndk-dir /Users/tberk/Library/Android/android-ndk-r16b/ --android-api 24 --arch=armeabi-v7a --ndk-version=r16b --requirements=python2


