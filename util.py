from azure.servicebus import ServiceBusService
from azure.servicebus import Message
def createSBS():
    service_namespace = 'FYPEventHub'
    key_name = "RootManageSharedAccessKey"
    key_value = 'kVUaa82ViZYNOQiPij2DuL2xGPOvbtv/Hu9VYcKriMk='
    sbs = ServiceBusService(service_namespace, shared_access_key_name=key_name, shared_access_key_value=key_value)
    return sbs

#This will get the Raspberry Pi 3 model B serial number
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial
