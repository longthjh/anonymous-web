#!/usr/bin/python


import time
import os
import subprocess


#####################-check-appps
try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 installed succesfully')
try:

    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

try:

    check_firefox = subprocess.check_output('which firefox', shell=True)
except subprocess.CalledProcessError:

    print('[+] firefox is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install firefox -y',shell=True)
    print('[!] firefox is installed succesfully ')

try:

    check_proxychains = subprocess.check_output('which proxychains', shell=True)
except subprocess.CalledProcessError:

    print('[+] proxychains is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install proxychains -y',shell=True)
    print('[!] proxychains  is installed succesfully ')

def change():
    os.system("service tor start && service tor reload")

##################################- start
os.system("clear")
print("\033[1;40;31m                               [!] please runing tools ussing sudo !!!\n")
time.sleep(5)
os.system("clear")
print('''\033[1;32;40m \n

▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·      ▄▄▄·  ▐ ▄        ▐ ▄  ▄· ▄▌• ▌ ▄ ·. ▄• ▄▌.▄▄ · 
██· █▌▐█▀▄.▀·▐█ ▀█▪    ▐█ ▀█ •█▌▐█▪     •█▌▐█▐█▪██▌·██ ▐███▪█▪██▌▐█ ▀. 
██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄    ▄█▀▀█ ▐█▐▐▌ ▄█▀▄ ▐█▐▐▌▐█▌▐█▪▐█ ▌▐▌▐█·█▌▐█▌▄▀▀▀█▄
▐█▌██▐█▌▐█▄▄▌██▄▪▐█    ▐█ ▪▐▌██▐█▌▐█▌.▐▌██▐█▌ ▐█▀·.██ ██▌▐█▌▐█▄█▌▐█▄▪▐█
 ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀      ▀  ▀ ▀▀ █▪ ▀█▄▀▪▀▀ █▪  ▀ • ▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀▀  [ FROM : longthjh2006005 ]

''')
print("\033[1;40;31m contact : longthjh2006005@fpt.edu.vn \n")
print("")
print("\033[1;32;40m Tools to keep you anonymous on your website and access the deepweb more easily than ever before \n")
time.sleep(3)
x = input("[+] time to change Ip in Sec >_  ")
lin = input("[+] how many time do you want to change your ip , for infinte ip change type >_ ")
os.system("firefox https://check.torproject.org/ https://www.dnsleaktest.com/")
if int(lin) ==int(0):

    while True:
        try:
            time.sleep(int(x))
            change()
        except KeyboardInterrupt:

            quit()

else:
    for i in range(int(lin)):
            time.sleep(int(x))
            change()
time.sleep(999999999999999999999999)
