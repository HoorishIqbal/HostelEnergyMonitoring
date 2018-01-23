import deviceToCloudMsgSender
import deviceManager
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

# Communication with Azure IoT Hub
connectionString = "HostName=HostelEnergyMonitoring.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=3FeEh3s8upgyY6j2ppjvHrCrpJyaKba5oQGXM+lUS9Y="
deviceToCloudMsgSender     = deviceToCloudMsgSender.DeviceToCloudMsgSender(connectionString)
deviceId = 'raspberry-pi'

"""HOST = ''
PORT = 6666 
serv = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv.bind((HOST, PORT))
print ("Bind ...")
serv.listen(1)
print "socket is listening"
while True:
    conn, addr = serv.accept()
    print ("Connection accepted. \n")"""

def sendData(deviceId, message):
	return (deviceToCloudMsgSender.sendD2CMsg(deviceId, message))

while 1:
		try:
			"""data  = conn.recv(512)
			data  = data.decode("utf-8")
			chunk = data.split(',')
			temperature  = float(chunk[0])
			x            = float(chunk[1])
			y            = float(chunk[2])
			z            = float(chunk[3])
			readData_idx = int(chunk[4])
			
			sent_time = str(datetime.utcnow())"""
			
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
                        message = {'deviceId': deviceId, 'voltage': voltage, 'current': current, 'power': power, 'sensor': sensor}
			message = json.dumps(message) 
			sendData(deviceId, message)
			
			conn = sqlite3.connect('/home/pi/HostelEnergyMonitoring.db')
			c = conn.cursor()
                        c.execute("INSERT INTO Reading (current_value, volts_value, power_value, sensor_id) VALUES (?, ?, ?, ?)",(current, voltage, power,sensor))
                        conn.commit()
                        print('data inserted.')

		except KeyboardInterrupt:
			conn.close()
			print ("bye!")
			sys.exit()

		except Exception:
			traceback.print_exc()
# conn.close()
