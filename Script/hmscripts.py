# -*- coding: utf-8

from urllib import urlencode
import urllib
import urllib2
import base64
import json

def executeHMScript(url, username, password, script):
	hmScript = script
	
	urlFull = "http://" + url + ":8181/Test.exe"
	
	print urlFull
	
	credentials = ('%s:%s' % (username, password))
	encoded_credentials = base64.b64encode(credentials.encode('ascii'))
	
	#postData = urllib.quote_plus(hmScript)  #hmScript  #urlencode(hmScript)
	postData = "var y=43;" + hmScript
	
	try:
		req = urllib2.Request(urlFull, postData)
		req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
		response = urllib2.urlopen(req).read()
	except:
		response = ""

	print "Answer from CCU: " + response

	return response





# http get request with Basic Authentication
#    req = urllib.request.Request(url)

#credentials = ('%s:%s' % (username, password))
#encoded_credentials = base64.b64encode(credentials.encode('ascii'))
#req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))

#text = urllib.request.urlopen(req).read()

#print('text: '+str(text))

# cut out the result from the returned XML
#variableContents = find_between(str(text), '<mySysVar>', '</mySysVar>')

#print('Answer from HM Script: ' + variableContents)

#return variableContents


g_testScript = "var x = 42;\n"+"var y = 43;\n"+"WriteLine('Cool');\n"+"WriteLine('Cooler');";


g_alarmScript = "var x = 42;\n"+"object o = dom.GetObject(ID_SERVICES);\n"+"string sDPID;\n"+\
	"Write('{');\n"+\
"var dpFirst = true;\n"+\
"foreach (sDPID, o.EnumIDs()) {\n"+\
"	object datapoint = dom.GetObject(sDPID);\n"+\
"    var trigDP = dom.GetObject(datapoint.AlTriggerDP());\n"+\
"    var chDP = trigDP.Channel();\n"+\
"  	if (dpFirst) {\n"+\
"    	dpFirst = false;\n"+\
"    } else {\n"+\
"      	WriteLine(',');\n"+\
"    }\n"+\
"  	Write('\"' # datapoint.ID() # '\":{');\n"+\
"  	Write('\"Name\":\"');\n"+\
"    WriteURL(datapoint.Name());\n"+\
"    Write('\",\"TypeName\":\"ALARMDP');\n"+\
"    Write('\",\"AlState\":' # datapoint.AlState());\n"+\
"    Write(',\"AlOccurrenceTime\":\"' # datapoint.AlOccurrenceTime());\n"+\
"    Write('\",\"LastTriggerTime\":\"' # datapoint.LastTriggerTime());\n"+\
"    Write('\",\"Operations\":' # trigDP.Operations());\n"+\
"    Write(',\"AlTriggerDP\":' # trigDP.ID());\n"+\
"    Write(',\"Parent\":' # chDP);\n"+\
"    Write('}');\n"+\
"}\n"+\
"WriteLine('}');";


g_favoritesScript = "var x = 42;\n"+\
"object oFavorite;\n" +\
"object fav;\n" +\
"string sFavoriteId;\n" +\
"string sFavoriteName;\n" +\
"string favId;\n" +\
"string chId;\n" +\
"boolean aFirst = true;\n" +\
"boolean bFirst;\n" +\
"Write('{');\n" +\
"foreach (sFavoriteId, dom.GetObject(ID_FAVORITES).EnumUsedIDs()) {\n" +\
"  oFavorite     = dom.GetObject(sFavoriteId);\n" +\
"  if (oFavorite.Name() == '_USER1004') {\n" +\
"    foreach(favId, oFavorite.EnumUsedIDs()) {\n" +\
"      if (aFirst) {\n" +\
"          aFirst = false;\n" +\
"      } else {\n" +\
"          WriteLine(',');\n" +\
"      }\n" +\
"      fav = dom.GetObject(favId);\n" +\
"      Write('\"' # favId # '\":{\"Name\":\"');\n" +\
"      WriteURL(fav.Name());\n" +\
"      Write('\",\"TypeName\":\"FAVORITE\",\"FavColumnCount\":' # fav.FavColumnCount());\n" +\
"      Write(',\"FavColumnAlign\":' # fav.FavColumnAlign());\n" +\
"      Write(',\"FavNamePosition\":' # fav.FavNamePosition());\n" +\
"      Write(',\"Channels\":[');\n" +\
"      bFirst = true;\n" +\
"      foreach (chId, fav.EnumUsedIDs()) {\n" +\
"     	if (bFirst) {\n" +\
"            bFirst = false;\n" +\
"        } else {\n" +\
"            Write(',');\n" +\
"        }\n" +\
"        Write(chId);\n" +\
"      }\n" +\
"      Write( ']}');\n" +\
"  	}\n" +\
"  }\n" +\
"}\n" +\
"WriteLine('}');";


g_roomsScript = "var x = 42;\n"+\
"object  oRoom;\n"+\
"string  sRoomId;\n"+\
"string  sChannelId;\n"+\
"boolean bFirst       = true;\n"+\
"boolean bFirstSecond = true;\n"+\
"\n"+\
"Write('{');\n"+\
"foreach (sRoomId, dom.GetObject(ID_ROOMS).EnumUsedIDs())\n"+\
"{\n"+\
"    if (bFirst == false) {\n"+\
"      WriteLine(',');\n"+\
"    } else {\n"+\
"      bFirst = false;\n"+\
"    }\n"+\
"    oRoom = dom.GetObject(sRoomId);\n"+\
"	Write('\"' # sRoomId # '\": ');\n"+\
"    Write('{\"Name\": \"');\n"+\
"    WriteURL(oRoom.Name());\n"+\
"    Write('\", \"TypeName\":\"' # oRoom.TypeName() # '_ROOMS');\n"+\
"    Write('\", \"EnumInfo\":\"');\n"+\
"    WriteURL(oRoom.EnumInfo());\n"+\
"    Write('\", \"Channels\":[');\n"+\
"	bFirstSecond = true;\n"+\
"    foreach(sChannelId, oRoom.EnumUsedIDs()) {\n"+\
"		if (bFirstSecond == false) {\n"+\
"		  Write(',');\n"+\
"		} else {\n"+\
"		  bFirstSecond = false;\n"+\
"		}\n"+\
"		Write(sChannelId);\n"+\
"    }\n"+\
"    Write(']}');\n"+\
"}\n"+\
"WriteLine('}');";


g_functionsScript = "var x = 42;\n"+\
"object  oFunction;\n"+\
"string  sFunctionId;\n"+\
"string  sChannelId;\n"+\
"boolean bFirst       = true;\n"+\
"boolean bFirstSecond = true;\n"+\
"\n"+\
"Write('{');\n"+\
"foreach (sFunctionId, dom.GetObject(ID_FUNCTIONS).EnumUsedIDs())\n"+\
"{\n"+\
"    if (bFirst == false) {\n"+\
"      WriteLine(',');\n"+\
"    } else {\n"+\
"      bFirst = false;\n"+\
"    }\n"+\
"    oFunction = dom.GetObject(sFunctionId);\n"+\
"	Write('\"' # sFunctionId # '\": ');\n"+\
"    Write('{\"Name\": \"');\n"+\
"    WriteURL(oFunction.Name());\n"+\
"    Write('\",\"TypeName\":\"' # oFunction.TypeName() # '_FUNCTIONS');\n"+\
"    Write('\", \"EnumInfo\": \"');\n"+\
"    WriteURL(oFunction.EnumInfo());\n"+\
"    Write('\", \"Channels\": [');\n"+\
"	bFirstSecond = true;\n"+\
"    foreach(sChannelId, oFunction.EnumUsedIDs()) {\n"+\
"		if (bFirstSecond == false) {\n"+\
"		  Write(',');\n"+\
"		} else {\n"+\
"		  bFirstSecond = false;\n"+\
"		}\n"+\
"		Write(sChannelId);\n"+\
"    }\n"+\
"    Write(']}');\n"+\
"}\n"+\
"WriteLine('}');";


g_variablesScript = "var x = 42;\n"+\
"object oSysVar;\n"+\
"string sSysVarId;\n"+\
"string sValueType;\n"+\
"string sValue;\n"+\
"boolean bFirst = true;\n"+\
"\n"+\
"Write('{');\n"+\
"\n"+\
"WriteLine('\"40\":{\"Name\":\"Alarmmeldungen\",\"TypeName\":\"VARDP\",\"DPInfo\":\"Anzahl%20Alarmmeldungen\",\"ValueMin\":0,\"ValueMax\":65000,\"ValueUnit\":\"\",\"ValueType\":16,\"ValueSubType\":0,\"ValueList\":\"\"},');\n"+\
"Write('\"41\":{\"Name\":\"Servicemeldungen\",\"TypeName\":\"VARDP\",\"DPInfo\":\"Anzahl%20Servicemeldungen\",\"ValueMin\":0,\"ValueMax\":65000,\"ValueUnit\":\"\",\"ValueType\":16,\"ValueSubType\":0,\"ValueList\":\"\"}');\n"+\
"\n"+\
"foreach (sSysVarId, dom.GetObject(ID_SYSTEM_VARIABLES).EnumUsedIDs()) {\n"+\
"\n"+\
"  WriteLine(',');\n"+\
"\n"+\
"  \n"+\
"  oSysVar     = dom.GetObject(sSysVarId); \n"+\
"  sValueType  = oSysVar.ValueType();\n"+\
"    \n"+\
"  Write('\"' # sSysVarId # '\":{\"Name\":\"');\n"+\
"  WriteURL(oSysVar.Name());\n"+\
"  Write('\",\"TypeName\":\"' # oSysVar.TypeName());\n"+\
"  Write('\",\"DPInfo\":\"');\n"+\
"  WriteURL(oSysVar.DPInfo());\n"+\
"\n"+\
"  Write('\",\"Value\":');\n"+\
"  if (sValueType == 20) {\n"+\
"    Write('\"');\n"+\
"  	WriteURL(oSysVar.Value());\n"+\
"    Write('\"');\n"+\
"  } else {\n"+\
"    sValue = oSysVar.Value();\n"+\
"    if (sValueType == 2) {\n"+\
"        if (sValue) {\n"+\
"            Write('true');\n"+\
"        } else {\n"+\
"            Write('false');\n"+\
"        }\n"+\
"    } else {\n"+\
"       if (sValue == '') {\n"+\
"            Write('0');\n"+\
"       } else {\n"+\
"            Write(sValue);\n"+\
"       }\n"+\
"    }\n"+\
"  }\n"+\
"  string sValueMin = oSysVar.ValueMin();\n"+\
"\n"+\
"  if (sValueMin == '') {\n"+\
"      sValueMin = 'null';\n"+\
"  }\n"+\
"\n"+\
"  string sValueMax = oSysVar.ValueMax();\n"+\
"\n"+\
"  if (sValueMax == '') {\n"+\
"      sValueMax = 'null';\n"+\
"  }\n"+\
"\n"+\
"  Write(',\"Timestamp\":\"' # oSysVar.Timestamp());\n"+\
"  Write('\",\"ValueMin\":' # sValueMin # ',\"ValueMax\":' # sValueMax # ',\"ValueUnit\":\"');\n"+\
"  WriteURL(oSysVar.ValueUnit());\n"+\
"  Write('\",\"ValueType\":' # sValueType # ',\"ValueSubType\":' # oSysVar.ValueSubType());\n"+\
"  \n"+\
"  if (sValueType == 2) {\n"+\
"    Write(',\"ValueList\":\"');\n"+\
"    WriteURL(oSysVar.ValueName0() # ';' # oSysVar.ValueName1());\n"+\
"  } else {\n"+\
"    Write(',\"ValueList\":\"');\n"+\
"    WriteURL(oSysVar.ValueList());\n"+\
"  }\n"+\
"\n"+\
"  Write('\"}');\n"+\
"  \n"+\
"}\n"+\
"\n"+\
"WriteLine('}');";


g_channelsScript = "var x = 42;\n"+\
"string sDevId;\n"+\
"string sChnId;\n"+\
"string sDPId;\n"+\
"string sDPName;\n"+\
"\n"+\
"Write('{');\n"+\
"\n"+\
"boolean dFirst = true;\n"+\
"boolean cFirst = true;\n"+\
"var counter = 0;\n"+\
"foreach (sDevId, root.Devices().EnumUsedIDs()) {\n"+\
"\n"+\
"    object oDevice   = dom.GetObject(sDevId);\n"+\
"    boolean bDevReady = oDevice.ReadyConfig();\n"+\
"    string sDevInterfaceId = oDevice.Interface();\n"+\
"    string sDevInterface   = dom.GetObject(sDevInterfaceId).Name();\n"+\
"\n"+\
"    if (bDevReady) {\n"+\
"\n"+\
"\n"+\
"        string sChnId;\n"+\
"        string sDPId;\n"+\
"\n"+\
"        foreach(sChnId, oDevice.Channels()) {\n"+\
"            object oChannel = dom.GetObject(sChnId);\n"+\
"            string sChnHssType = oChannel.HssType();\n"+\
"                if (cFirst) {\n"+\
"                  cFirst = false;\n"+\
"                } else {\n"+\
"                  Write(',');\n"+\
"                }\n"+\
"\n"+\
"                integer iChnDir = oChannel.ChnDirection();\n"+\
"                Write('\"' # sChnId # '\":{\"Name\":\"');\n"+\
"                WriteURL(oChannel.Name());\n"+\
"                Write('\",\"TypeName\":\"' # oChannel.TypeName());\n"+\
"                Write('\",\"HssType\":\"' # sChnHssType);\n"+\
"                Write('\",\"ChnDirection\":' # iChnDir # ',\"ChannelType\":');\n"+\
"                Write(oChannel.ChannelType());\n"+\
"                Write('\",\"Address\":\"' # oChannel.Address());\n"+\
"                Write('\",\"ChnLabel\":\"' # oChannel.ChnLabel());\n"+\
"                Write('\",\"Parent\":' # sDevId);\n"+\
"                Write('\",\"DPs\":{');\n"+\
"\n"+\
"                boolean dpFirst = true;\n"+\
"\n"+\
"                if (iChnDir == 2) {\n"+\
"                    object oWork = oChannel.DPByHssDP('WORKING');\n"+\
"                    if (oWork) {\n"+\
"                        dpFirst = false;\n"+\
"                        string oWId = oWork.ID();\n"+\
"                        Write('\"WORKING\":'#oWId);\n"+\
"                    }\n"+\
"                    object oDir = oChannel.DPByHssDP('DIRECTION');\n"+\
"                    if (oDir) {\n"+\
"                        if (dpFirst) {\n"+\
"                          dpFirst = false;\n"+\
"                        } else {\n"+\
"                          Write(',');\n"+\
"                        }\n"+\
"                        string oDirId = oDir.ID();\n"+\
"                        Write('\"DIRECTION\":'#oDirId);\n"+\
"                    }\n"+\
"                }\n"+\
"\n"+\
"\n"+\
"                foreach(sDPId, oChannel.DPs().EnumUsedIDs()) {\n"+\
"                    object oDP = dom.GetObject(sDPId);\n"+\
"                    if (oDP.TypeName() == 'VARDP') {\n"+\
"                        sDPName = oDP.Name();\n"+\
"                    } else {\n"+\
"                        sDPName = oDP.Name().StrValueByIndex('.', 2);\n"+\
"                    }\n"+\
"                    if(oDP) {\n"+\
"                        if (dpFirst) {\n"+\
"                          dpFirst = false;\n"+\
"                        } else {\n"+\
"                          Write(',');\n"+\
"                        }\n"+\
"                        Write('\"');\n"+\
"                        WriteURL(sDPName);\n"+\
"                        Write('\":'#sDPId);\n"+\
"                    }\n"+\
"                }\n"+\
"                Write('}}');\n"+\
"\n"+\
"        }\n"+\
"\n"+\
"    }\n"+\
"}\n"+\
"WriteLine('}');";


g_devicesScript = "var x = 42;\n"+\
"\n"+\
"string sDevId;\n"+\
"string sChnId;\n"+\
"string sDPId;\n"+\
"\n"+\
"Write('{');\n"+\
"\n"+\
"    boolean dFirst = true;\n"+\
"\n"+\
"    foreach (sDevId, root.Devices().EnumUsedIDs()) {\n"+\
"\n"+\
"\n"+\
"    object oDevice   = dom.GetObject(sDevId);\n"+\
"    boolean bDevReady = oDevice.ReadyConfig();\n"+\
"    string sDevInterfaceId = oDevice.Interface();\n"+\
"    string sDevInterface   = dom.GetObject(sDevInterfaceId).Name();\n"+\
"\n"+\
"    if (oDevice.HssType() == '') { } else {\n"+\
"    if (bDevReady) {\n"+\
"\n"+\
"        if (dFirst) {\n"+\
"          dFirst = false;\n"+\
"        } else {\n"+\
"          WriteLine(',');\n"+\
"        }\n"+\
"\n"+\
"        Write('\"' # sDevId # '\":{\"Name\":\"');\n"+\
"        WriteURL(oDevice.Name());\n"+\
"        Write('\",\"TypeName\":\"' # oDevice.TypeName());\n"+\
"        Write('\",\"HssType\":\"' # oDevice.HssType() # '\",\"Address\":\"' # oDevice.Address() # '\",\"Interface\":\"' # sDevInterface);\n"+\
"        Write('\",\"Channels\":[');\n"+\
"\n"+\
"        string sChnId;\n"+\
"\n"+\
"        boolean cFirst = true;\n"+\
"        foreach(sChnId, oDevice.Channels()) {\n"+\
"            if (cFirst) {\n"+\
"                cFirst = false;\n"+\
"            } else {\n"+\
"                Write(',');\n"+\
"            }\n"+\
"            Write(sChnId);\n"+\
"        }\n"+\
"        Write(']}');\n"+\
"    }\n"+\
"    }\n"+\
"}\n"+\
"WriteLine('}');\n";


def testHMScripts():
	answer1 = executeHMScript("", g_testScript)
	answer2 = executeHMScript("", g_alarmScript)
	answer3 = executeHMScript("", g_favoritesScript)
	answer4 = executeHMScript("", g_roomsScript)
	answer5 = executeHMScript("", g_functionsScript)
	answer6 = executeHMScript("", g_variablesScript)
	answer7 = executeHMScript("", g_channelsScript)
	answer8 = executeHMScript("", g_devicesScript)
	
	return answer1 + answer2 + answer3 + answer4 + answer5 + answer6 + answer7 + answer8



def testParseResults():
	
	# Teil der Antwort des Scripts oben, answer4 (Räume)
	resultDemo = """
		{"1234": {"Name": "Aussen", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[13127,13152,3356,3350,3636,15696,15699,6206,6209,3486,2293,13195]}, "1231": {"Name": "Bad%20EG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[3147,9849,9702,4415,9657,4412,9697,9707,9931,9926,9921,9893,9897,4477,8894]}, "1229": {"Name": "Bad%2BWC%20OG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[5812,5809,5806,4111,2457,4240,2505,2849,2850,4237,2483,9011,4170,4180,4192,4302,2822,8853]}, "1233": {"Name": "Balkon%20OG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[8985]}, "1230": {"Name": "Buero%20OG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[3085,3116,5934,5931,9415,3225,9397,9403,9409,9588,5960]}, "1590": {"Name": "Eingangsbereich%20KG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[7629,9846,11646,9843,11652,6062,6059,12064,10243,10193,10198,10208,10223,10218,10203,10213,10238,10233,10228,9631,12490,6024,1171,9619,9623,9627,2126,2129,2134]}, "1226": {"Name": "Essen%2BKueche%20EG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[1341,1353,1347,1365,1359,1335,9125,2660,2691,3895,3901,3195,15527,10098,9119,3173,15524,10078,9255,10083,10093,10088,11513,10006,9978,9968,9963,9958,9973,10001,9991,10011,9996,10030,10034,10038,10042,11520,15489,15554]}, "1591": {"Name": "Freiraum%20DG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[10332,10329,13572,13575,7405,2602,7230,5202]}, "1592": {"Name": "Gaestebereich%20DG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[3982,3979]}, "1232": {"Name": "Garage%20KG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[9846,3775,12024,6120,6117,9292,3770,3767,12490,3793]}, "1594": {"Name": "Heizraum%20KG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[4753]}, "1589": {"Name": "Keller%20KG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[6091,6088,7562]}, "1228": {"Name": "Kinderzimmer%20OG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[5291,5285,5261,5273,5279,5267,9858,1579,5998,5340,5995,5334,5376,5328,5322,5474,3254,15657]}, "1593": {"Name": "Labor%20DG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[10335,4008,7236,7136,8397,7269,7263,1175,1179]}, "1588": {"Name": "Lagerraum%20KG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[6146,9298]}, "1597": {"Name": "Schaltschrank%20EG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[9174,9182]}, "1227": {"Name": "Schlafzimmer%20OG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[5848,5845,9861,1796,1789,1786,1783,1541,2880,2982,2959,5876,1721,1710,1707,1704,3283,2906]}, "1596": {"Name": "Stiegenhaus%20EG-OG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[6579,6357,1207,1211,4046,1398,1392,1410,1404,1422,1416,1434,1428,1446,1440,1458,1452,1470,1464,7460,9336,7328,7322]}, "1595": {"Name": "Stiegenhaus%20KG-EG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[14234,14226,14242,14250,6579,7629,7662,7601]}, "1235": {"Name": "Terrasse%20EG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[8517,8523,8125,8119,8143,8149,8131,8137,11922,8979,8244,8216,9852,1183,1187]}, "1225": {"Name": "Wohnzimmer%20EG", "TypeName":"ENUM_ROOMS", "EnumInfo":"", "Channels":[8490,8466,8460,8478,8472,8484,7751,8071,1293,1287,9855,4590,9809,9804,9814,9799,4587,9794,9819,10299,10267,10271,10275,10279,10283,10287,10291,10295,9852,4652,1199,1203,1191,1195]}}
		"""
	
	# Teil der Antwort des Scripts oben, answer5 (Gewerke)
	resultDemo2 = """
		
		{"1755": {"Name": "Beschattung","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [1796,1789,6579,6357,7751,8071,8244,8216,5474,1721,1710,7136]}, "1224": {"Name": "Energiemanagement","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [3775,3895,3901,8403,8410,8412,8414,8416,9809,9804,9799,10098,9119,3356,3350,3486,9397,9403,9409,8397,3770,9174,9182,3767,3793,2422,2718,2391,5202,2129,2134]}, "8555": {"Name": "frei","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [9261,9107,9113,3480,3492,3498,11658,11664,5340,9936,9940,9901,9905,9909,9913,9917,9983,9987,10248,10303,10307,10311,9649,9685,9689,9693,9712,9717,9722,9727,9653,9661,9665,9669,9673,9677,9681,9746,9782,9786,9790,9824,9750,9754,9758,9762,9766,9770,9774,9778,10066,10070,10074,10103,10108,10046,10050,10054,10058,10062,9592,9596,9601,9873,9876,10356,10359,10362,10338,10341,10344,10347,10350,10353]}, "1216": {"Name": "Heizung","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [9702,4415,4535,4240,4360,5934,6062,6120,6091,5998,15527,4011,4590,4710,2602,3173,2959,2483,4753,4477,4302,5960,6024,15657,15489,2906,2822,4652]}, "1217": {"Name": "Klima","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [13572,13575,4412,4237,5931,2602,6059,3979,6117,6088,5995,3173,15524,4008,6146,2959,2483,4587]}, "1215": {"Name": "Licht","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [9125,9814,8979,5334,9415,7230,10078,5376,9697,9794,9707,12064,9255,9292,7562,7236,9298,5328,5876,5322,7460,7601,8985,10083,10093,10088,9819,9011,4170,4180,4192,2061,2068]}, "1220": {"Name": "Sicherheit","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [14234,14226,14242,14250,13127,13152,7629,1579,1541,7662,11922,5812,9846,9849,9855,11646,9843,11652,3225,9341,3254,3283,9336,9867,9864,9870,11513,11520,9852,12490,1171,15554,8894,8853,9619,9623,9627]}, "10475": {"Name": "Status","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [9931,9926,9921,10243,10193,10198,10208,10223,10218,10203,10213,10238,10233,10228,10006,9978,9968,9963,9958,9973,10001,9991,10011,9996]}, "1222": {"Name": "Taster","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [5848,5845,8517,8523,1341,1353,1347,1365,1359,1335,5291,5285,5261,5273,5279,5267,8125,8119,8143,8149,8131,8137,8490,8466,8460,8478,8472,8484,1786,1783,1207,1211,5809,5806,1293,1287,1398,1392,1410,1404,1422,1416,1434,1428,1446,1440,1458,1452,1470,1464,14795,14801,14804,14798,12289,12295,12292,12298,14837,14840,14834,14831,1299,1301,1302,1303,1304,1305,1476,1482,1488,1494,1500,1506,9657,15696,15699,1707,1704,9893,9897,9588,9631,10030,10034,10038,10042,7269,7263,7328,7322,10299,10267,10271,10275,10279,10283,10287,10291,10295,1183,1187,1199,1203,1191,1195,1175,1179,2126,2058]}, "1219": {"Name": "Umwelt","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [3636]}, "1221": {"Name": "Verschluss","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [9858,9861,4111,4046,10335,2457,9846,3147,9849,3085,3116,2660,2691,10332,2880,10329,9855,12024,9843,4555,4380,4730,9873,9876,9852,12490]}, "2988": {"Name": "Visu","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [9125,9858,9861,6579,6357,8071,1579,1541,4111,4046,10335,2457,9846,3147,9849,3085,3116,2660,2691,10332,2880,10329,9855,12024,9843,9107,10098,4412,4237,5931,2602,6059,3979,6117,6088,5995,3173,15524,4008,6146,2959,2483,4587,8979,5334,9415,7230,10078,5376,9697,9794,9707,12064,9255,9292,7562,7236,9298,5328,5876,5322,7460,7601,8985,10083,10093,10088,9819,9011,8244,8216,3356,3350,3636,7136,3486,9852,12490,2906,2822,2293,13195]}, "1218": {"Name": "Wetter","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [13127,13152,7405,6206,6209,2293,13195]}, "1223": {"Name": "Zentrale","TypeName":"ENUM_FUNCTIONS", "EnumInfo": "", "Channels": [1015,1051,1055,1059,1063,1067,1071,1075,1079,1083,1087,1019,1091,1095,1099,1103,1107,1111,1115,1119,1123,1127,1023,1131,1135,1139,1143,1147,1151,1155,1159,1163,1167,1027,1031,1035,1039,1043,1047,9424,9451,9454,9457,9460,9463,9466,9469,9472,9475,9478,9427,9481,9484,9487,9490,9493,9496,9499,9502,9505,9508,9430,9511,9514,9517,9520,9523,9526,9529,9532,9535,9538,9433,9541,9544,9547,9550,9553,9556,9559,9562,9565,9568,9436,9571,9439,9442,9445,9448]}}
		"""
	
	
	# resultDemo ist eine Datenstruktur für Räume, die von der CCU 1:1 zurückkommt, wenn man es richtig macht.
	# mit dieser einen Zeile mache ich daraus ein Python-Dictionary:
	pythonDataStructureRooms = json.loads(resultDemo)
	
	# dictionary auf einen Schlag ausgeben, was uns aber nichts bringt:
	#print pythonDataStructureRooms
	
	print "\n\n\n"
	
	# und dann der einfache Zugriff auf alle Räume und ihre IDs und Kanäle (Python 2.x, in Python 3.x wäre es nur items(), dann geht es aber nicht als iOS-App.):
	# = iterieren durch keys und values (hier id, room) des dictionaries
	for id, room in pythonDataStructureRooms.iteritems():
		print "Room " + room["Name"] + " has the ID " + str(id) + "\nChannels in this Room:\n"
		
		channelsString = ""
		for channel in room["Channels"]:
			channelsString += str(channel) + ", "
		print channelsString + "\n\n"
	
	
	
	# dasselbe für Gewerke
	pythonDataStructureFunctions = json.loads(resultDemo2)

	#print pythonDataStructureFunctions
	print "\n\n\n"
	
	# und dann der einfache Zugriff auf alle Gewerke und ihre IDs und Kanäle (Python 2.x):
	# = iterieren durch keys und values (hier id, room) des dictionaries
	for id, function in pythonDataStructureFunctions.iteritems():
		print "Function category " + function["Name"] + " has the ID " + str(id) + "\nChannels in this Function category:\n"

		channelsString = ""
		for channel in function["Channels"]:
			channelsString += str(channel) + ", "
		print channelsString + "\n\n"

	# genauso kriegt man mit diesen wenigen Zeilen Code alle Favoriten, Kanäle, Geräte, und man weiß welche Kanäle in welchen Geräten sind. -> alles bereit zum ausfüllen der Seiten, parsen mit den IDs der Datenpunkte, die auch hier drinstehen.


	# Beispiel für einen Kanal
	channelExample = """
		{"Name":"Heizung Wohnzimmer","TypeName":"CHANNEL","HssType":"CLIMATECONTROL_RT_TRANSCEIVER","ChnDirection":0,"ChannelType":17,"Address":"INT0000005:1","ChnLabel":"CLIMATECONTROL_RT_TRANSCEIVER","Parent":4698,"DPs":{"CONTROL_MODE":4716,"ACTUAL_HUMIDITY":4711,"BOOST_MODE":4714,"AUTO_MODE":4713,"SET_TEMPERATURE":4729,"ACTUAL_TEMPERATURE":4712,"MANU_MODE":4718,"COMFORT_MODE":4715,"LOWERING_MODE":4717,"PARTY_TEMPERATURE":4728,"PARTY_START_TIME":4722,"PARTY_START_DAY":4720,"PARTY_START_MONTH":4721,"PARTY_START_YEAR":4723,"PARTY_STOP_TIME":4726,"PARTY_STOP_DAY":4724,"PARTY_STOP_MONTH":4725,"PARTY_STOP_YEAR":4727,"PARTY_MODE_SUBMIT":4719}
		}
		"""

	oneChannel = json.loads(channelExample)
	
	print "\n\nKanal " + oneChannel["Name"] + " hat folgende Daten:\n"
	for id, channelData in oneChannel.iteritems():
		print id + ": " + str(channelData)


	print "\n\nThis channel belongs to the device with the ID: " + str(oneChannel["Parent"]) + "\n"

	print "\n\nDatapoints and their IDs: \n"
	for datapoint, id in oneChannel["DPs"].iteritems():
		print "\n" + str(datapoint) + ": " + str(id)






#
# new code for getting device list
#



# old offline data for testing without CCU
testResultFromCCU = """{"9879":{"Name":"12-IO%20Bad%20EG","TypeName":"DEVICE","HssType":"HMW-IO-12-FM","Address":"HEQ0165221","Interface":"BidCos-Wired","Channels":[9880,9893,9897,9901,9905,9909,9913,9917,9921,9926,9931,9936,9940]}, "10179":{"Name":"12-IO%20Eingangsbereich","TypeName":"DEVICE","HssType":"HMW-IO-12-FM","Address":"IEQ0532489","Interface":"BidCos-Wired","Channels":[10180,10193,10198,10203,10208,10213,10218,10223,10228,10233,10238,10243,10248]}, "9944":{"Name":"12-IO%20Esszimmer","TypeName":"DEVICE","HssType":"HMW-IO-12-FM","Address":"HEQ0165274","Interface":"BidCos-Wired","Channels":[9945,9958,9963,9968,9973,9978,9983,9987,9991,9996,10001,10006,10011]}, "10253":{"Name":"12-IO%20Wohnzimmer","TypeName":"DEVICE","HssType":"HMW-IO-12-FM","Address":"JEQ0080737","Interface":"BidCos-Wired","Channels":[10254,10267,10271,10275,10279,10283,10287,10291,10295,10299,10303,10307,10311]}, "10315":{"Name":"12-Kanal-Schliesserkontakt%20DG","TypeName":"DEVICE","HssType":"HMW-Sen-SC-12-DR","Address":"KEQ0167634","Interface":"BidCos-Wired","Channels":[10316,10329,10332,10335,10338,10341,10344,10347,10350,10353,10356,10359,10362]}, "9829":{"Name":"12-Kanal-Schliesserkontakt%20EG","TypeName":"DEVICE","HssType":"HMW-Sen-SC-12-DR","Address":"HEQ0024998","Interface":"BidCos-Wired","Channels":[9830,9843,9846,9849,9852,9855,9858,9861,9864,9867,9870,9873,9876]}, "8496":{"Name":"2fach%20Taster%20Terrasse","TypeName":"DEVICE","HssType":"HM-PB-2-WM55","Address":"JEQ0005231","Interface":"BidCos-RF","Channels":[8497,8517,8523]}, "5821":{"Name":"2K-Taster%20Schlafzimmer","TypeName":"DEVICE","HssType":"HMIP-WRC2","Address":"000193C98CA55E","Interface":"HmIP-RF","Channels":[5822,5845,5848]}, "9574":{"Name":"4-IO%20Buero","TypeName":"DEVICE","HssType":"HMW-IO-4-FM","Address":"EEQ0048578","Interface":"BidCos-Wired","Channels":[9575,9588,9592,9596,9601]}, "9605":{"Name":"4-IO%20Eingangsbereich","TypeName":"DEVICE","HssType":"HMW-IO-4-FM","Address":"EEQ0048683","Interface":"BidCos-Wired","Channels":[9606,9619,9623,9627,9631]}, "9372":{"Name":"4K-Aktor%20Buero","TypeName":"DEVICE","HssType":"HM-LC-Sw4-DR","Address":"IEQ0168742","Interface":"BidCos-RF","Channels":[9373,9397,9403,9409,9415]}, "11621":{"Name":"4K-Aktor%20Eingangsbereich","TypeName":"DEVICE","HssType":"HM-LC-Sw4-DR","Address":"MEQ0582682","Interface":"BidCos-RF","Channels":[11622,11646,11652,11658,11664]}, "5297":{"Name":"4K-Aktor%20Kinderzimmer","TypeName":"DEVICE","HssType":"HM-LC-Sw4-DR","Address":"NEQ0193154","Interface":"BidCos-RF","Channels":[5298,5322,5328,5334,5340]}, "9082":{"Name":"4K-Aktor%20Kueche","TypeName":"DEVICE","HssType":"HM-LC-Sw4-DR","Address":"IEQ0168321","Interface":"BidCos-RF","Channels":[9083,9107,9113,9119,9125]}, "1306":{"Name":"6fach%20Taster%20Essen%20EG","TypeName":"DEVICE","HssType":"HM-PB-6-WM55","Address":"KEQ0631162","Interface":"BidCos-RF","Channels":[1307,1335,1341,1347,1353,1359,1365]}, "8090":{"Name":"6fach%20Taster%20Terrasse","TypeName":"DEVICE","HssType":"HM-PB-6-WM55","Address":"KEQ0631517","Interface":"BidCos-RF","Channels":[8091,8119,8125,8131,8137,8143,8149]}, "8431":{"Name":"6fach%20Taster%20Wohnzimmer","TypeName":"DEVICE","HssType":"HM-PB-6-WM55","Address":"KEQ0631295","Interface":"BidCos-RF","Channels":[8432,8460,8466,8472,8478,8484,8490]}, "5232":{"Name":"6fach-Taster%20Kinderzimer","TypeName":"DEVICE","HssType":"HM-PB-6-WM55","Address":"KEQ0631513","Interface":"BidCos-RF","Channels":[5233,5261,5267,5273,5279,5285,5291]}, "14185":{"Name":"Alarmsirene%20innen","TypeName":"DEVICE","HssType":"HM-Sec-Sir-WM","Address":"MEE0000285","Interface":"BidCos-RF","Channels":[14186,14226,14234,14242,14250]}, "15672":{"Name":"Audi%20Q5","TypeName":"DEVICE","HssType":"HMIP-WRC2","Address":"000193C98CA536","Interface":"HmIP-RF","Channels":[15673,15696,15699]}, "1756":{"Name":"Beschattungsaktor%20Schlafzimmer","TypeName":"DEVICE","HssType":"HmIP-FROLL","Address":"00115702625A98","Interface":"HmIP-RF","Channels":[1757,1783,1786,1789,1796,1804,1812,1820]}, "6558":{"Name":"Beschattungsaktor%20Stgh%20EG","TypeName":"DEVICE","HssType":"HM-LC-Bl1-FM","Address":"JEQ0047887","Interface":"BidCos-RF","Channels":[6559,6579]}, "6336":{"Name":"Beschattungsaktor%20Stgh%20OG","TypeName":"DEVICE","HssType":"HM-LC-Bl1-PB-FM","Address":"IEQ0148208","Interface":"BidCos-RF","Channels":[6337,6357]}, "7730":{"Name":"Beschattungsaktor%20Wohnzimmer%20Fenster","TypeName":"DEVICE","HssType":"HM-LC-Bl1-FM","Address":"JEQ0048677","Interface":"BidCos-RF","Channels":[7731,7751]}, "8050":{"Name":"Beschattungsaktor%20Wohnzimmer%20Tuer","TypeName":"DEVICE","HssType":"HM-LC-Bl1-FM","Address":"MEQ0212054","Interface":"BidCos-RF","Channels":[8051,8071]}, "7607":{"Name":"Bewegungsmelder%20Eingangsbereich","TypeName":"DEVICE","HssType":"HM-Sen-MDIR-O","Address":"JEQ0738799","Interface":"BidCos-RF","Channels":[7608,7629]}, "7633":{"Name":"Bewegungsmelder%20Stgh%20KG","TypeName":"DEVICE","HssType":"HmIP-SMI","Address":"00091569927D1F","Interface":"HmIP-RF","Channels":[7634,7662]}, "11900":{"Name":"Bewegungsmelder%20Terrasse","TypeName":"DEVICE","HssType":"HM-Sen-MDIR-SM","Address":"HEQ0161661","Interface":"BidCos-RF","Channels":[11901,11922]}, "13106":{"Name":"Bewegungssensor%20Markise%20links","TypeName":"DEVICE","HssType":"HM-Sec-TiS","Address":"LEQ0787216","Interface":"BidCos-RF","Channels":[13107,13127]}, "13131":{"Name":"Bewegungssensor%20Markise%20rechts","TypeName":"DEVICE","HssType":"HM-Sec-TiS","Address":"LEQ0786680","Interface":"BidCos-RF","Channels":[13132,13152]}, "1550":{"Name":"BWM%20Kinderzimmer","TypeName":"DEVICE","HssType":"HmIP-SPI","Address":"000C17099A00C5","Interface":"HmIP-RF","Channels":[1551,1579,1587]}, "1512":{"Name":"BWM%20Schlafzimmer","TypeName":"DEVICE","HssType":"HmIP-SPI","Address":"000C17099A00CA","Interface":"HmIP-RF","Channels":[1513,1541,1549]}, "5781":{"Name":"BWM%20WC%20OG","TypeName":"DEVICE","HssType":"HmIP-SMI55","Address":"0014D709AEF88E","Interface":"HmIP-RF","Channels":[5782,5806,5809,5812,5820]}, "9635":{"Name":"Controller%20Bad%20EG","TypeName":"DEVICE","HssType":"HMW-IO-12-Sw7-DR","Address":"FEQ0045915","Interface":"BidCos-Wired","Channels":[9636,9649,9653,9657,9661,9665,9669,9673,9677,9681,9685,9689,9693,9697,9702,9707,9712,9717,9722,9727]}, "10016":{"Name":"Controller%20Kueche","TypeName":"DEVICE","HssType":"HMW-IO-12-Sw7-DR","Address":"IEQ0241905","Interface":"BidCos-Wired","Channels":[10017,10030,10034,10038,10042,10046,10050,10054,10058,10062,10066,10070,10074,10078,10083,10088,10093,10098,10103,10108]}, "9732":{"Name":"Controller%20Wohnzimmer","TypeName":"DEVICE","HssType":"HMW-IO-12-Sw7-DR","Address":"FEQ0046071","Interface":"BidCos-Wired","Channels":[9733,9746,9750,9754,9758,9762,9766,9770,9774,9778,9782,9786,9790,9794,9799,9804,9809,9814,9819,9824]}, "13544":{"Name":"Differenztemperatursensor%20Globe","TypeName":"DEVICE","HssType":"HM-WDS30-OT2-SM","Address":"KEQ0102442","Interface":"BidCos-RF","Channels":[13545,13572,13575,13578,13581,13584]}, "1258":{"Name":"Display%20Pool%20und%20Heizung","TypeName":"DEVICE","HssType":"HM-Dis-EP-WM55","Address":"NEQ0712140","Interface":"BidCos-RF","Channels":[1259,1287,1293,1299,1301,1302,1303,1304,1305]}, "1371":{"Name":"Display-Wandtaster%20OG","TypeName":"DEVICE","HssType":"HM-PB-4Dis-WM-2","Address":"NEQ1486914","Interface":"BidCos-RF","Channels":[1372,1392,1398,1404,1410,1416,1422,1428,1434,1440,1446,1452,1458,1464,1470,1476,1482,1488,1494,1500,1506]}, "9145":{"Name":"Energiez%E4hler","TypeName":"DEVICE","HssType":"HM-ES-TX-WM","Address":"MEQ0025575","Interface":"BidCos-RF","Channels":[9146,9174,9182]}, "14771":{"Name":"FB%20Nicole","TypeName":"DEVICE","HssType":"HmIP-KRCA","Address":"00099709A0E11C","Interface":"HmIP-RF","Channels":[14772,14795,14798,14801,14804]}, "12265":{"Name":"FB%20Robert","TypeName":"DEVICE","HssType":"HmIP-KRCA","Address":"000995698BD979","Interface":"HmIP-RF","Channels":[12266,12289,12292,12295,12298]}, "14807":{"Name":"FB%20Sarah","TypeName":"DEVICE","HssType":"HmIP-KRCA","Address":"00099709A0E25E","Interface":"HmIP-RF","Channels":[14808,14831,14834,14837,14840]}, "3118":{"Name":"Fenstersensor%20Bad%20EG","TypeName":"DEVICE","HssType":"HmIP-SRH","Address":"0007D5699E95A3","Interface":"HmIP-RF","Channels":[3119,3147]}, "4082":{"Name":"Fenstersensor%20Bad%20OG","TypeName":"DEVICE","HssType":"HM-Sec-SCo","Address":"MEQ1658402","Interface":"BidCos-RF","Channels":[4083,4111]}, "3056":{"Name":"Fenstersensor%20Buero%20links","TypeName":"DEVICE","HssType":"HmIP-SRH","Address":"0007D5699E9227","Interface":"HmIP-RF","Channels":[3057,3085]}, "3087":{"Name":"Fenstersensor%20Buero%20rechts","TypeName":"DEVICE","HssType":"HmIP-SRH","Address":"0007D5699E9143","Interface":"HmIP-RF","Channels":[3088,3116]}, "2631":{"Name":"Fenstersensor%20Esszimmer%20links","TypeName":"DEVICE","HssType":"HmIP-SWDO-I","Address":"00109709A3BD5D","Interface":"HmIP-RF","Channels":[2632,2660]}, "2662":{"Name":"Fenstersensor%20Kueche%20rechts","TypeName":"DEVICE","HssType":"HmIP-SWDO-I","Address":"00109709A3BDAB","Interface":"HmIP-RF","Channels":[2663,2691]}, "2851":{"Name":"Fenstersensor%20Schlafzimmer","TypeName":"DEVICE","HssType":"HmIP-SRH","Address":"0007D5699E9147","Interface":"HmIP-RF","Channels":[2852,2880]}, "4017":{"Name":"Fenstersensor%20Stgh%20OG","TypeName":"DEVICE","HssType":"HMIP-SWDO","Address":"0000D3C98C9F92","Interface":"HmIP-RF","Channels":[4018,4046]}, "2428":{"Name":"Fenstersensor%20WC%20OG","TypeName":"DEVICE","HssType":"HMIP-SWDO","Address":"0000D3C98CA005","Interface":"HmIP-RF","Channels":[2429,2457]}, "3866":{"Name":"Geschirrspueler-Aktor","TypeName":"DEVICE","HssType":"HM-ES-PMSw1-DR","Address":"NEQ0116960","Interface":"BidCos-RF","Channels":[3867,3895,3901,3908,3910,3912,3914]}, "4523":{"Name":"Heizung%20Bad%20EG%20INT0000004","TypeName":"DEVICE","HssType":"HM-CC-VG-1","Address":"INT0000004","Interface":"VirtualDevices","Channels":[4524,4535,4555]}, "4348":{"Name":"Heizung%20Bad%20OG%20INT0000003","TypeName":"DEVICE","HssType":"HM-CC-VG-1","Address":"INT0000003","Interface":"VirtualDevices","Channels":[4349,4360,4380]}, "4698":{"Name":"Heizung%20Wohnzimmer%20INT0000005","TypeName":"DEVICE","HssType":"HM-CC-VG-1","Address":"INT0000005","Interface":"VirtualDevices","Channels":[4699,4710,4730]}, "16390":{"Name":"Heizungsgruppe%20DG%20INT0000006","TypeName":"DEVICE","HssType":"HmIP-HEATING","Address":"INT0000006","Interface":"VirtualDevices","Channels":[16391,16421,16448,16449,16451,16456]}, "2989":{"Name":"Heizungsgruppe%20Schlafzimmer%20INT0000002","TypeName":"DEVICE","HssType":"HmIP-HEATING","Address":"INT0000002","Interface":"VirtualDevices","Channels":[2990,3020,3047,3048,3050,3055]}, "2511":{"Name":"Heizungsgruppe%20WC%20OG%20INT0000001","TypeName":"DEVICE","HssType":"HmIP-HEATING","Address":"INT0000001","Interface":"VirtualDevices","Channels":[2512,2542,2569,2570,2572,2577]}, "7376":{"Name":"Helligkeitssensor%20West","TypeName":"DEVICE","HssType":"HM-Sen-LI-O","Address":"NEQ0322404","Interface":"BidCos-RF","Channels":[7377,7405]}, "12465":{"Name":"Keymatic%20Garage","TypeName":"DEVICE","HssType":"HM-Sec-Key-S","Address":"HEQ0407468","Interface":"BidCos-RF","Channels":[12466,12490]}, "6126":{"Name":"Klimasensor%20Lagerraum","TypeName":"DEVICE","HssType":"HM-WDS10-TH-O","Address":"JEQ0015970","Interface":"BidCos-RF","Channels":[6127,6146]}, "7205":{"Name":"Lichtaktor%20Dachgeschoss","TypeName":"DEVICE","HssType":"HM-LC-Sw2-FM","Address":"IEQ0073081","Interface":"BidCos-RF","Channels":[7206,7230,7236]}, "12031":{"Name":"Lichtaktor%20Eingangsbereich","TypeName":"DEVICE","HssType":"HM-LC-Sw1-DR","Address":"MEQ1510791","Interface":"BidCos-RF","Channels":[12032,12064]}, "9230":{"Name":"Lichtaktor%20Esszimmer%20Decke","TypeName":"DEVICE","HssType":"HM-LC-Sw2-FM","Address":"HEQ0113538","Interface":"BidCos-RF","Channels":[9231,9255,9261]}, "9267":{"Name":"Lichtaktor%20Garage","TypeName":"DEVICE","HssType":"HM-LC-Sw2-FM","Address":"IEQ0072903","Interface":"BidCos-RF","Channels":[9268,9292,9298]}, "7529":{"Name":"Lichtaktor%20Keller","TypeName":"DEVICE","HssType":"HM-LC-Sw1-DR","Address":"MEQ0276649","Interface":"BidCos-RF","Channels":[7530,7562]}, "5851":{"Name":"Lichtaktor%20Schlafzimmer","TypeName":"DEVICE","HssType":"HM-LC-Sw1-FM","Address":"IEQ0344105","Interface":"BidCos-RF","Channels":[5852,5876]}, "7431":{"Name":"Lichtaktor%20Stgh%20EG-OG","TypeName":"DEVICE","HssType":"HM-LC-Dim1T-DR","Address":"NEQ1743679","Interface":"BidCos-RF","Channels":[7432,7460,7483,7506]}, "7568":{"Name":"Lichtaktor%20Stgh%20KG-EG","TypeName":"DEVICE","HssType":"HM-LC-Sw1-DR","Address":"MEQ1510820","Interface":"BidCos-RF","Channels":[7569,7601]}, "8954":{"Name":"Lichtaktor%20Terrasse%2FBalkon","TypeName":"DEVICE","HssType":"HM-LC-Sw2-FM","Address":"IEQ0004861","Interface":"BidCos-RF","Channels":[8955,8979,8985]}, "8991":{"Name":"Lichtaktor%20WC%20OG%20HM","TypeName":"DEVICE","HssType":"HM-LC-Dim1T-FM","Address":"IEQ0381504","Interface":"BidCos-RF","Channels":[8992,9011]}, "5347":{"Name":"Lichtdimmer%20Decke%20Kinderzimmer","TypeName":"DEVICE","HssType":"HM-LC-Dim1TPBU-FM","Address":"JEQ0250793","Interface":"BidCos-RF","Channels":[5348,5376,5399,5422]}, "8223":{"Name":"Markisenaktor%20Terrasse%20links","TypeName":"DEVICE","HssType":"HM-LC-Bl1-SM","Address":"LEQ0136712","Interface":"BidCos-RF","Channels":[8224,8244]}, "8195":{"Name":"Markisenaktor%20Terrasse%20rechts","TypeName":"DEVICE","HssType":"HM-LC-Bl1-SM","Address":"LEQ0136707","Interface":"BidCos-RF","Channels":[8196,8216]}, "4732":{"Name":"Mischeraktor%20Heizraum","TypeName":"DEVICE","HssType":"HM-LC-Bl1-SM","Address":"EEQ0045446","Interface":"BidCos-RF","Channels":[4733,4753]}, "11480":{"Name":"MP3-Funkgong","TypeName":"DEVICE","HssType":"HM-OU-CFM-Pl","Address":"IEQ0533351","Interface":"BidCos-RF","Channels":[11481,11513,11520]}, "3455":{"Name":"Poolaktor","TypeName":"DEVICE","HssType":"HM-LC-Sw4-DR","Address":"KEQ0093596","Interface":"BidCos-RF","Channels":[3456,3480,3486,3492,3498]}, "3616":{"Name":"Poolsensor","TypeName":"DEVICE","HssType":"HM-WDS30-T-O","Address":"FEQ0031533","Interface":"BidCos-RF","Channels":[3617,3636]}, "3321":{"Name":"Poolverbrauchsaktor","TypeName":"DEVICE","HssType":"HM-ES-PMSw1-DR","Address":"MEQ0421376","Interface":"BidCos-RF","Channels":[3322,3350,3356,3363,3365,3367,3369]}, "5445":{"Name":"Raffstoreaktor%20Kinderzimmer","TypeName":"DEVICE","HssType":"HM-LC-Ja1PBU-FM",
	"Address":"MEQ0483863","Interface":"BidCos-RF","Channels":[5446,5474]},
	"1677":{"Name":"Raffstoreaktor%20Schlafzimmer","TypeName":"DEVICE","HssType":"HmIP-BBL","Address":"001357098D4216","Interface":"HmIP-RF","Channels":[1678,1704,1707,1710,1721,1731,1741,1751]}, "3201":{"Name":"Rauchsensor%20Buero","TypeName":"DEVICE","HssType":"HmIP-SWSD","Address":"000A58A98A00DE","Interface":"HmIP-RF","Channels":[3202,3225]}, "9339":{"Name":"Rauchsensor%20HM%20Gruppe","TypeName":"DEVICE","HssType":"HM-Sec-SD-Team","Address":"*HEQ0403667","Interface":"BidCos-RF","Channels":[9340,9341]}, "3230":{"Name":"Rauchsensor%20Kinderzimmer","TypeName":"DEVICE","HssType":"HmIP-SWSD","Address":"000A58A98A021E","Interface":"HmIP-RF","Channels":[3231,3254]}, "3259":{"Name":"Rauchsensor%20Schlafzimmer","TypeName":"DEVICE","HssType":"HmIP-SWSD","Address":"000A58A98A0227","Interface":"HmIP-RF","Channels":[3260,3283]}, "9304":{"Name":"Rauchsensor%20Stgh%20OG","TypeName":"DEVICE","HssType":"HM-Sec-SD","Address":"HEQ0403667","Interface":"BidCos-RF","Channels":[9305,9336]}, "6181":{"Name":"Regensensor","TypeName":"DEVICE","HssType":"HM-Sen-RD-O","Address":"KEQ0884222","Interface":"BidCos-RF","Channels":[6182,6206,6209]}, "4137":{"Name":"RGBW-Aktor%20Bad%20OG","TypeName":"DEVICE","HssType":"HM-LC-RGBW-WM","Address":"MEQ1097270","Interface":"BidCos-RF","Channels":[4138,4170,4180,4192]}, "12003":{"Name":"Rollladenaktor%20Garage","TypeName":"DEVICE","HssType":"HM-LC-Bl1-SM","Address":"LEQ0802038","Interface":"BidCos-RF","Channels":[12004,12024]}, "7115":{"Name":"Rollladenaktor%20Labor","TypeName":"DEVICE","HssType":"HM-LC-Bl1-FM","Address":"MEQ1894680","Interface":"BidCos-RF","Channels":[7116,7136]}, "7242":{"Name":"Taster%20Labor","TypeName":"DEVICE","HssType":"HM-PB-2-WM55","Address":"KEQ0362659","Interface":"BidCos-RF","Channels":[7243,7263,7269]}, "7301":{"Name":"Taster%20Stgh%20OG","TypeName":"DEVICE","HssType":"HM-PB-2-WM55","Address":"KEQ0362747","Interface":"BidCos-RF","Channels":[7302,7322,7328]}, "5940":{"Name":"Ventilaktor%20Buero","TypeName":"DEVICE","HssType":"HM-CC-VD","Address":"FEQ0030969","Interface":"BidCos-RF","Channels":[5941,5960]}, "6004":{"Name":"Ventilaktor%20Eingangsbereich","TypeName":"DEVICE","HssType":"HM-CC-VD","Address":"HEQ0147791","Interface":"BidCos-RF","Channels":[6005,6024]}, "15637":{"Name":"Ventilaktor%20Kinderzimmer","TypeName":"DEVICE","HssType":"HM-CC-VD","Address":"IEQ0173213","Interface":"BidCos-RF","Channels":[15638,15657]}, "15469":{"Name":"Ventilaktor%20Kueche","TypeName":"DEVICE","HssType":"HM-CC-VD","Address":"GEQ0162914","Interface":"BidCos-RF","Channels":[15470,15489]}, "2882":{"Name":"Ventilaktor%20Schlafzimmer","TypeName":"DEVICE","HssType":"HMIP-eTRV","Address":"000393C98D1C09","Interface":"HmIP-RF","Channels":[2883,2906,2929,2930,2931,2932,2933,2934]}, "2798":{"Name":"Ventilaktor%20WC%20OG","TypeName":"DEVICE","HssType":"HMIP-eTRV","Address":"000393C98D18B0","Interface":"HmIP-RF","Channels":[2799,2822,2845,2846,2847,2848,2849,2850]}, "4619":{"Name":"Ventilaktor%20Wohnzimmer","TypeName":"DEVICE","HssType":"HM-CC-RT-DN","Address":"MEQ1880485","Interface":"BidCos-RF","Channels":[4620,4649,4650,4651,4652,4696,4697]}, "4444":{"Name":"Ventilator%20Bad%20EG","TypeName":"DEVICE","HssType":"HM-CC-RT-DN","Address":"KEQ0516538","Interface":"BidCos-RF","Channels":[4445,4474,4475,4476,4477,4521,4522]}, "4269":{"Name":"Ventilator%20Bad%20OG","TypeName":"DEVICE","HssType":"HM-CC-RT-DN","Address":"MEQ1880470","Interface":"BidCos-RF","Channels":[4270,4299,4300,4301,4302,4346,4347]}, "13084":{"Name":"VIR-HUE-GTW%20HU-Philips%20hue","TypeName":"DEVICE","HssType":"VIR-HUE-GTW","Address":"HU-Philips hue","Interface":"VirtualDevices","Channels":[13085,13086]}, "13100":{"Name":"VIR-LG-RGBW-DIM%20HU-Eingangsber","TypeName":"DEVICE","HssType":"VIR-LG-RGBW-DIM","Address":"HU-Eingangsber","Interface":"VirtualDevices","Channels":[13101,13102]}, "1012":{"Name":"virtuelle%20BidCoS-RF%20Tasten","TypeName":"DEVICE","HssType":"HM-RCV-50","Address":"BidCoS-RF","Interface":"BidCos-RF","Channels":[1013,1015,1019,1023,1027,1031,1035,1039,1043,1047,1051,1055,1059,1063,1067,1071,1075,1079,1083,1087,1091,1095,1099,1103,1107,1111,1115,1119,1123,1127,1131,1135,1139,1143,1147,1151,1155,1159,1163,1167,1171,1175,1179,1183,1187,1191,1195,1199,1203,1207,1211]}, "9422":{"Name":"virtuelle%20BidCoS-Wired%20Tasten","TypeName":"DEVICE","HssType":"HMW-RCV-50","Address":"BidCoS-Wir","Interface":"BidCos-Wired","Channels":[9423,9424,9427,9430,9433,9436,9439,9442,9445,9448,9451,9454,9457,9460,9463,9466,9469,9472,9475,9478,9481,9484,9487,9490,9493,9496,9499,9502,9505,9508,9511,9514,9517,9520,9523,9526,9529,9532,9535,9538,9541,9544,9547,9550,9553,9556,9559,9562,9565,9568,9571]}, "4382":{"Name":"Wandthermostat%20Bad%20EG","TypeName":"DEVICE","HssType":"HM-TC-IT-WM-W-EU","Address":"LEQ0001455","Interface":"BidCos-RF","Channels":[4383,4412,4415,4440,4441,4442]}, "4207":{"Name":"Wandthermostat%20Bad%20OG","TypeName":"DEVICE","HssType":"HM-TC-IT-WM-W-EU","Address":"LEQ0000275","Interface":"BidCos-RF","Channels":[4208,4237,4240,4265,4266,4267]}, "5911":{"Name":"Wandthermostat%20Buero","TypeName":"DEVICE","HssType":"HM-CC-TC","Address":"FEQ0030808","Interface":"BidCos-RF","Channels":[5912,5931,5934,5939]}, "2578":{"Name":"Wandthermostat%20Dachgeschoss","TypeName":"DEVICE","HssType":"HMIP-WTH","Address":"000313C98CC3A3","Interface":"HmIP-RF","Channels":[2579,2602,2625,2626,2627,2628,2629,2630]}, "6039":{"Name":"Wandthermostat%20Eingangsbereich","TypeName":"DEVICE","HssType":"HM-CC-TC","Address":"HEQ0145629","Interface":"BidCos-RF","Channels":[6040,6059,6062,6067]}, "3959":{"Name":"Wandthermostat%20Gaestebereich","TypeName":"DEVICE","HssType":"HM-CC-TC","Address":"IEQ0170889","Interface":"BidCos-RF","Channels":[3960,3979,3982,3987]}, "6097":{"Name":"Wandthermostat%20Garage","TypeName":"DEVICE","HssType":"HM-CC-TC","Address":"IEQ0170865","Interface":"BidCos-RF","Channels":[6098,6117,6120,6125]}, "6068":{"Name":"Wandthermostat%20Keller","TypeName":"DEVICE","HssType":"HM-CC-TC","Address":"IEQ0106628","Interface":"BidCos-RF","Channels":[6069,6088,6091,6096]}, "5975":{"Name":"Wandthermostat%20Kinderzimmer","TypeName":"DEVICE","HssType":"HM-CC-TC","Address":"HEQ0510203","Interface":"BidCos-RF","Channels":[5976,5995,5998,6003]}, "3149":{"Name":"Wandthermostat%20Kueche","TypeName":"DEVICE","HssType":"HmIP-STHD","Address":"000E9709931296","Interface":"HmIP-RF","Channels":[3150,3173,3195,3196,3197,3198,3199,3200]}, "15504":{"Name":"Wandthermostat%20Kueche%20HM","TypeName":"DEVICE","HssType":"HM-CC-TC","Address":"HEQ0510349","Interface":"BidCos-RF","Channels":[15505,15524,15527,15532]}, "3988":{"Name":"Wandthermostat%20Labor","TypeName":"DEVICE","HssType":"HM-CC-TC","Address":"KEQ0355932","Interface":"BidCos-RF","Channels":[3989,4008,4011,4016]}, "2935":{"Name":"Wandthermostat%20Schlafzimmer","TypeName":"DEVICE","HssType":"HMIP-WTH","Address":"000313C98CC415","Interface":"HmIP-RF","Channels":[2936,2959,2982,2983,2984,2985,2986,2987]}, "2459":{"Name":"Wandthermostat%20WC%20OG","TypeName":"DEVICE","HssType":"HmIP-STHD","Address":"000E970993124F","Interface":"HmIP-RF","Channels":[2460,2483,2505,2506,2507,2508,2509,2510]}, "4557":{"Name":"Wandthermostat%20Wohnzimmer","TypeName":"DEVICE","HssType":"HM-TC-IT-WM-W-EU","Address":"MEQ0478717","Interface":"BidCos-RF","Channels":[4558,4587,4590,4615,4616,4617]}, "8873":{"Name":"Wassersensor%20Bad%20EG","TypeName":"DEVICE","HssType":"HM-Sec-WDS-2","Address":"GEQ0143528","Interface":"BidCos-RF","Channels":[8874,8894]}, "8832":{"Name":"Wassersensor%20Bad%20OG","TypeName":"DEVICE","HssType":"HM-Sec-WDS-2","Address":"GEQ0143598","Interface":"BidCos-RF","Channels":[8833,8853]}, "15533":{"Name":"Wassersensor%20Kueche","TypeName":"DEVICE","HssType":"HM-Sec-WDS-2","Address":"GEQ0143555","Interface":"BidCos-RF","Channels":[15534,15554]}, "13167":{"Name":"Wettersensor%20HM","TypeName":"DEVICE","HssType":"HM-WDS100-C6-O","Address":"JEQ0735632","Interface":"BidCos-RF","Channels":[13168,13195]}, "2265":{"Name":"Wetterstation","TypeName":"DEVICE","HssType":"HmIP-SWO-PR","Address":"00185709A8E8DA","Interface":"HmIP-RF","Channels":[2266,2293,2314,2315,2316,2317,2318,2319,2320]}, "2397":{"Name":"Zwischenstecker%201","TypeName":"DEVICE","HssType":"HM-LC-Sw1-Pl-2","Address":"FEQ0061848","Interface":"BidCos-RF","Channels":[2398,2422]}, "2693":{"Name":"Zwischenstecker%202","TypeName":"DEVICE","HssType":"HM-LC-Sw1-Pl-2","Address":"IEQ0343559","Interface":"BidCos-RF","Channels":[2694,2718]}, "2366":{"Name":"Zwischenstecker%203","TypeName":"DEVICE","HssType":"HM-LC-Sw1-Pl-2","Address":"IEQ0343560","Interface":"BidCos-RF","Channels":[2367,2391]}, "5175":{"Name":"Zwischenstecker%20DG%20DB22","TypeName":"DEVICE","HssType":"HMIP-PS","Address":"000213C98DDB22","Interface":"HmIP-RF","Channels":[5176,5202,5205,5210,5216,5222,5228]}, "3747":{"Name":"Zwischenstecker%20Entfeuchter%20Garage","TypeName":"DEVICE","HssType":"HMIP-PSM","Address":"0001D3C98DD8A0","Interface":"HmIP-RF","Channels":[3748,3767,3770,3775,3781,3787,3793,3804]}, "2099":{"Name":"Zwischenstecker%20IP%20DBE3","TypeName":"DEVICE","HssType":"HMIP-PS","Address":"000213C98DDBE3","Interface":"HmIP-RF","Channels":[2100,2126,2129,2134,2140,2146,2152]}, "2029":{"Name":"Zwischenstecker%20IP%20dimmbar","TypeName":"DEVICE","HssType":"HmIP-PDT","Address":"000DD7098B90F1","Interface":"HmIP-RF","Channels":[2030,2058,2061,2068,2077,2086,2095]}, "8368":{"Name":"Zwischenstecker%20SONOS%20Amps","TypeName":"DEVICE","HssType":"HM-ES-PMSw1-Pl","Address":"KEQ0966022","Interface":"BidCos-RF","Channels":[8369,8397,8403,8410,8412,8414,8416]}} /Test.exe
	User-Agent: Python-urllib/2.74283688416falseZwischenstecker SONOS Ampstrue1009BidCos-RFfalse"""



def getDeviceList(testPrint):
	
	url = "1501.2.meine-homematic.de"
	username = "franzhelmli2"
	passwd = "cool2pi"
	
	resultFromCCU = executeHMScript(url, username, passwd, g_devicesScript)
	resultFromCCUCutOffToJSON = ""
	
	# if CCU really returned something, use it, else show the test data
	#if "}}" not in resultFromCCU:
	#	k = testResultFromCCU.rfind("}}") + 2
	#	resultFromCCUCutOffToJSON = testResultFromCCU[:k]
	#else:
	k = resultFromCCU.rfind("}}") + 2
	resultFromCCUCutOffToJSON = resultFromCCU[:k]
	
	#print testResultFromCCU
	
	
	pythonDataStructureDevices = json.loads(resultFromCCUCutOffToJSON)
	
	#print pythonDataStructureDevices
	
	
	# Zugriff auf alle Geräte und ihre IDs und Namen usw. (Python 2.x, in Python 3.x wäre es nur items(), dann geht es aber nicht als App)
	for id, device in pythonDataStructureDevices.iteritems():
		try:
			device["Name"] = urllib.unquote(device["Name"]) #.decode('utf_8')
		except:
			pass #print "can't decode the evil string: " + device["Name"]
		
		if testPrint:
			print "Device with the id " + str(id) + " has the Name '" + device["Name"] + "'\nThis device has the following usable name for polling (just add ':' + 'channel.datapoint' for all 'channel.datapoint' strings returned by the SVG class of this device): " + device["Interface"]+"."+device["Address"] + "\nThe type of this device (for looking in the SVG Table which one to use and finding out the channel.datapoint combinations to poll and visualize!) is '" + device["HssType"] + "'\n\n"

	return pythonDataStructureDevices


###

# getting devices from the CCU at 10.0.0.2
#devices = getDeviceList(True)


#usage of this dictionary 'devices':
#for id, device in devices.iteritems():
#		use the variable id (Key) and the 3 members of a device (Value):
#		device["Name"], device["Interface"]+"."+device["Address"] and device["HssType"]

# without the interface and address, how can you poll its values? Answer: you can't. the ID of a device has no use, only the IDs of Datapoints, which we don't have here.

###


# old tests
#cool = testHMScripts()
#print cool

#testParseResults()

