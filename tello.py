#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time
import platform  

host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

sent = sock.sendto(b'command', tello_address)
print ("command")
sent = sock.sendto(b'takeoff', tello_address)
print ("takeoff")
time.sleep(5)
sent = sock.sendto(b'forward 10', tello_address)
print ("forward 20")
time.sleep(5)
sent = sock.sendto(b'flip f', tello_address)
print ("flip f")
time.sleep(5)
sent = sock.sendto(b'back 10', tello_address)
print ("back 20")
time.sleep(5)
sent = sock.sendto(b'land', tello_address)