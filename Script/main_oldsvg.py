#!/usr/bin/env python2

import ui, os
import threading
import socket
import SimpleHTTPServer
import BaseHTTPServer
import time

hostName = ""
hostPort = 8081

BaseHTTPRequestHandler = SimpleHTTPServer.SimpleHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):

	#	GET is for clients geting the predi
	def do_GET(self):
		self.send_response(200, 'OK')
		self.send_header('Content-type', 'html')
		self.end_headers()
		
		self.wfile.write(bytes("<html><body>"))
		
		for x in range(1000):
			self.wfile.write(bytes("""
				<h1>This WebView content was written in Python! Additional data sent from Python code: %s<p><p>And here an SVG file:</h1>
				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 68 65">
				<path fill="#1A374D" d="M42 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v21l12 15-7 15.7c14.5 13.9 35 2.8 35-13.7 0-13.3-13.4-21.8-26-18zm6 25c-3.9 0-7-3.1-7-7s3.1-7 7-7 7 3.1 7 7-3.1 7-7 7z"/>
				<path d="M14 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v41c0 8.2 9.2 17 20 17s20-9.2 20-20c0-13.3-13.4-21.8-26-18zm6 25c-3.9 0-7-3.1-7-7s3.1-7 7-7 7 3.1 7 7-3.1 7-7 7z"/>
				</svg>
				
				
			""" % str(x))) # self.path, "utf-8"))
		
		#time.sleep(2.0)
		
		myServer.server_close()

		
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
	
	
	
t = threading.Thread(target=worker, args=(0,))
t.daemon = True
t.start()

#time.sleep(1.0)



file_path = os.path.abspath('html/main.html')

v = ui.load_view()

v['webview1'].load_url('http://localhost:' + str(hostPort) + '/test1234')

#v['webview1'].load_url(file_path)

v.present(style='sheet', title_bar_color='#000000',
#hide_close_button=True,
hide_title_bar=True,
orientations=['portrait'])


# HTML zu Python: (User-Events, Seite geladen): Ajax zum HTTP-Server

# Python zu HTML: Ajax in Dauerschleife, wenn Jacascript-Antwort von Python kommt: dieses ausfuehren

#Editier-stuff: native UI-Elemente mit der Portablen LIb fuer Kivy und Pythonista ueber dem WebView einblenden

#Translation-File in Python, das alles auch im HTML und SVG uebersetzt, HTML und SVG muessen Englisch sein
