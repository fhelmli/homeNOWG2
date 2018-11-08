# -*- coding: utf-8 

dictionary = {
	"homeNOW": "homeNOW",
	"Dashboard": "Dashboard",
	"HomeIndicator": "HomeIndicator",
	"Menu": "Menü","
	"Rooms": "Räume",
	"Functions": "Gewerke",
	"Favorites": "Favoriten",
	"Device": "Gerät",
	"Devices": "Geräte",
	"Channel": "Kanal",
	"Channels": "Kanäle",
	
	"Settings": "Einstellungen",
	"Edit Page": "Seite Editieren","
	"Username": "Benutzername",
	"Password": "Passwort",
	"IP Address": "IP-Adresse",
	"or": "oder",
	"and": "und",
	"Server address": "Server-Adresse",
	"": ""
}

def tr(word, language=None):
	if language==None or language=="de":
		return dictionary[word]
	else:
		return word
	
