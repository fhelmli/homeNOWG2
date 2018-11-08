# -*- coding: utf-8 

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

def tr(word, language=None):
	if language==None or language=="de":
		return dictionaryDE[word]
	else:
		return word
	
