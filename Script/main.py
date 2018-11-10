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


from pageviewcontroller import worker


#######################################################
# our new bundle ID for iOS App: at.homenow.homenow2
#######################################################


	
if inAnApp:
	t = threading.Thread(target=worker, args=(0,))
	t.daemon = True
	t.start()
	
	#time.sleep(1.0)
	
	file_path = os.path.dirname(sys.executable) + '/Script/html/main.html'
	if "Pythonista3" in file_path:
		file_path = os.path.abspath('html/main.html')
	else:
		f = ObjCClass('NSBundle').mainBundle().resourcePath()
		print f + "\n\n"
		
		#docpath = str(f.URLsForDirectory_inDomains_(9,1)[0].path())
		docpath = f
		
		file_path = docpath + '/Script/html/main.html'
	
	print file_path
	
	print os.path.realpath(__file__)

	v = ui.load_view()
	
	#v['webview1'].load_url('http://localhost:' + str(hostPort) + '/oachkatzlschwoaf0815')
	
	v['webview1'].load_url(file_path)
	
	v.present(style='sheet', title_bar_color='#000000',
	#hide_close_button=True,
	hide_title_bar=True,
	animated=False)
	#orientations=['portrait'])

else:
	worker(0)


# HTML zu Python: (User-Events, Seite geladen): Ajax zum HTTP-Server

# Python zu HTML: Ajax in Dauerschleife, wenn Jacascript-Antwort von Python kommt: dieses ausfuehren

# events von SVGs und buttons etc. zu Python, und z.B. redrawWidget, redrawWindow, redrawPage-events ueber Ajax u Python

#Editier-stuff: native UI-Elemente mit der Portablen LIb fuer Kivy und Pythonista ueber dem WebView einblenden

#Translation-File in Python, das alles auch im HTML und SVG uebersetzt, HTML und SVG muessen Englisch sein
