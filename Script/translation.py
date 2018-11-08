# -*- coding: utf-8 

dictionary = {
	"Rooms": "Räume",
	"Functions": "Gewerke",
	"Favorites": "Favoriten",
	"Device": "Gerät",
	"Devices": "Geräte",
	"Channel": "Kanal",
	"Channels": "Kanäle"
}

def tr(word, language=None):
	if language==None or language=="de":
		return dictionary[word]
	else:
		return word
	
