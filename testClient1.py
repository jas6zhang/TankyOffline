# Message Sender
from socket import *
import time
host = "10.96.192.52" # target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    
    time.sleep(3)

    words = input ("data test")
    print ("sent" +data)
    data = words.read()
    UDPSock.sendto(bytes(data, 'utf_8'), addr)
    if data == "exit":
        break

    
        
UDPSock.close()

