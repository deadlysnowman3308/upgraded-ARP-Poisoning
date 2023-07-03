# upgraded-ARP-Poisoning

```
   CVE-2021-29280
```

### After running this tool, wait for 1-2 minutes then automatically your Internet will be disconnected !!
### All connected devices also can't connect to the internet.

<br>

## What is ARP-Poisoning?

- ARP Poisoning (also known as ARP Spoofing) is a type of cyber attack carried out over a Local Area Network (LAN) that involves sending malicious ARP packets to a default gateway on a LAN in order to change the pairings in its IP to MAC address table. ARP Protocol translates IP addresses into MAC addresses. Because the ARP protocol was designed purely for efficiency and not for security, ARP Poisoning attacks are extremely easy to carry out as long as the attacker has control of a machine within the target LAN or is directly connected to it.

- The attack itself consists of an attacker sending a false ARP reply message to the default network gateway, informing it that his or her MAC address should be associated with his or her target's IP address (and vice-versa, so his or her target's MAC is now associated with the attacker's IP address). Once the default gateway has received this message and broadcasts its changes to all other devices on the network, all of the target's traffic to any other device on the network travels through the attacker's computer, allowing the attacker to inspect or modify it before forwarding it to its real destination. Because ARP Poisoning attacks occur on such a low level, users targeted by ARP Poisoning rarely realize that their traffic is being inspected or modified. Besides Man-in-the-Middle Attacks, ARP Poisoning can be used to cause a denial-of-service condition over a LAN by simply intercepting or dropping and not forwarding the target's packets.

<br>

- This powerful Python script harnesses the strength of SYN packets to generate a flood of network activity. 🌩️⚡

- With the help of the Scapy library, this code allows you to initiate a high-intensity flood by simulating the initiation of TCP connections. 💥💣

- The SYN Flooder offers a straightforward interface, allowing you to specify the target host or IP address. Once launched, the script deploys multiple threads 🧵 to enhance the flooding effect, overwhelming the target with a surge of connection requests. 🌊🌪️

Please exercise caution and use this tool responsibly. SYN flooding is an aggressive network testing technique that should only be employed in controlled environments with proper authorization. ⚠️🔒

We encourage you to explore this repository, learn about network security, and contribute to its development. Together, let's build a safer and more resilient cyberspace. 💪🌟

## Note: It's crucial to respect legal and ethical boundaries while using this code.

### :: Installation ::

```
$ git clone https://github.com/deadlysnowman3308/upgraded-ARP-Poisoning

$ cd upgraded-ARP-Poisoning

$ sudo chmod +x *

$ sudo pip3 install requirements.txt
```

### :: Usage ::

```
$ sudo python3 upgraded-ARP-Poisoning.py

```
<br>

[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.linux.org/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Kali_Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)](https://www.kali.org/)
[![Linux_mint](https://img.shields.io/badge/Linux_Mint-87CF3E?style=for-the-badge&logo=linux-mint&logoColor=white)](https://linuxmint.com/)


<br>

* Note: After turn off this tool, your internet should be online. If not then restart your router !!

```
  CVE-2021-29280
```

<br>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

</br>

Created by:>   [Aniket Dinda](https://hackingvila.wordpress.com/)
