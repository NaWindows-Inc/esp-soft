from bluepy.btle import Scanner, DefaultDelegate
from datetime import datetime
import requests

address = "app-flask-backend.herokuapp.com/api/bledata/upload"

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

for dev in devices:
    print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
    for (adtype, desc, value) in dev.getScanData():
        print "  %s = %s" % (desc, value)
        
    data = {'mac': dev.addr, 'level': dev.rssi, 'time':str(datetime.now())} 
    headers = {'Content-Type': 'application/json'}
    print data
    url_post = 'http://{}/api/bledata/upload'.format(address)
    response = requests.post(url_post, headers=headers, json=data)
    print "RESPONSE STATUS: %s " % (response.status_code)   
