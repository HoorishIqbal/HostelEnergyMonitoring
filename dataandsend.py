#import deviceToCloudMsgSender
#import deviceManager
import json 
import socket
from time import *
import sys
import sqlite3
import traceback
from datetime import datetime
import random
#import requests
import urllib
import urllib2
import sys
import util
sbs = util.createSBS()
iD = util.getserial()
while 1:
    url='$,220,'
    cc=random.random()*10
    pw=cc*220
    url2=url+str(int(cc))+ ','+str(int(pw))+',' 
    print url2
    #date = datetime.date.today()
    #time = datetime.time(1, 2, 3)
    pieces = url2.split(',')
    voltage = float(pieces[1])
    current = float(pieces[2])
    power = float(pieces[3])
    sensor = 1
    message = {'voltage': voltage, 'current': current, 'power': power, 'sensor': sensor}
    message = json.dumps(message) 
    print(message)
    sbs.send_event('fypeventhub', message)			
                        
