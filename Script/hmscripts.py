# -*- coding: utf-8

from urllib import urlencode
import urllib2
import base64
import json

def executeHMScript(url, script):
    hmScript = script
    
    username = 'tberk'
    password = 'tom1977'
    url = "http://10.0.0.2:8181/Test.exe"

    #url = "http://" + url + ":8181/Test.exe?" + hmScript
    
    #print('url: '+url)
    #username = 'franzhelmli2'
    #password = 'cool2pi'
    
    #username='admin'
    #password=''
    
    credentials = ('%s:%s' % (username, password))
    encoded_credentials = base64.b64encode(credentials.encode('ascii'))

    post = hmScript  #urlencode(hmScript)
    req = urllib2.Request(url, post)
    req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
    response = urllib2.urlopen(req).read()
    
    #print response
    
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

	# und dann der einfache Zugriff auf alle Räume und ihre Kanäle (Python 2.x, in Python 3.x wäre es nur items(), dann geht es aber nicht als iOS-App.):
	for id, rooms in pythonDataStructureRooms.iteritems():
		print "Room " + rooms["Name"] + " has the ID " + str(id) + "\nChannels in this Room:\n"

		channelsString = ""
		for channel in rooms["Channels"]:
			channelsString += str(channel) + ", "
		print channelsString + "\n\n"


	pythonDataStructureFunctions = json.loads(resultDemo2)

	#print pythonDataStructureFunctions
				
	print "\n\n\n"
		
	
	# und dann der einfache Zugriff auf alle Gewerke und ihre Kanäle (Python 2.x):
	for id, functions in pythonDataStructureFunctions.iteritems():
		print "Function category " + functions["Name"] + " has the ID " + str(id) + "\nChannels in this Function category:\n"

		channelsString = ""
		for channel in functions["Channels"]:
			channelsString += str(channel) + ", "
		print channelsString + "\n\n"

	# genauso kriegt man mit diesen wenigen Zeilen Code alle Favoriten, Kanäle, Geräte, und man weiß welche Kanäle in welchen Geräten sind. -> alles bereit zum ausfüllen der Seiten, parsen mit den IDs der Datenpunkte, die auch hier drinstehen.

#cool = testHMScripts()

testParseResults()
