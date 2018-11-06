from urllib import urlencode
import urllib2
import base64

def executeHMScript(url, script):
    hmScript = script
    
    username = 'tberk'
    password = 'tom1977'
    url2 = "https://home.peissl.at/rega/Test.exe?" + hmScript
    url = "https://home.peissl.at/rega/Test.exe"

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

#cool = testHMScripts()
