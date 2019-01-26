import settings
import hmdevices
import hmdevice
import hmccu
import hminterface
import model


s=settings.settings(1)
s.printc()

i=hminterface.hmInterface(s)
ccu=hmccu.hmCCU(i)
ccu.updateConfig()
m=model.model(ccu)
m.generateDeviceClasses()
m.printc()
m.updateAll()

