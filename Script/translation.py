# -*- coding: utf-8 

import config

#
# TODO: Add many more words needed for the App! Now I added only some words for the first visualisation
#
dictionaryDE = {
	"homeNOW": "homeNOW",
	"Dashboard": "Dashboard",
	"HomeIndicator": "HomeIndicator",
	"Menu": "Menü",
	"Rooms": "Räume",
	"Functions": "Gewerke",
	"Favorites": "Favoriten",
	"Device": "Gerät",
	"Devices": "Geräte",
	"Channel": "Kanal",
	"Channels": "Kanäle",
	
	"Settings": "Einstellungen",
	"Edit Page": "Seite Editieren",
	"Username": "Benutzername",
	"Password": "Passwort",
	"IP Address": "IP-Adresse",
	"or": "oder",
	"and": "und",
	"Server address": "Server-Adresse",
	"Empty": "Leer",
	"empty": "leer",
	"Empty Widget": "Leeres Widget",
	"Window": "Fenster",
	"Window Title": "Fenstertitel",
	

}

def setGlobalLanguage(language):
	config.g_language = language
	
def tr(word, language=None):
	if language==None:
		if config.g_language=="de":
			return dictionaryDE[word]
		else:
			return word
	else:
		if language=="de": 		
			return dictionaryDE[word]
		else:
			return word
	
