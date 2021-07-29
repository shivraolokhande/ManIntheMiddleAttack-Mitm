

<p align="center">
    <img src="https://user-images.githubusercontent.com/71170862/127441173-7746645d-9826-468d-bbd8-618505bb791e.jpg" alt="mitmlogo">
</p>

<h3 align="center">MITM</h3>

<p align="center">
  This repository includes source codes to achieve Man In the Middle Attack effectively using python3 script to perform DNS spoofing via ARP poisoning attached along with Project Report and Screenshots
</p>

# Installation
```console
kali@shiv:~$ git clone https://github.com/blackeko/mitm/
kali@shiv:~$ cd mitm
kali@shiv:~$ pip3 install -r requirements.txt
kali@shiv:~$ sudo python3 mitm.py
```
Man In The Middle Attack project includes DNS spoof module to alter DNS records that are used
to redirect online traffic to a fraudulent website that resembles its intended destination and ARP
spoof module to linking of an attacker's MAC address with the IP address of a legitimate computer
or server on the network.

# Tools and Technologies Used :
* **Bettercap** or Ettercap is a man-in-the-middle (MITM) attack tool developed for users who
are likely to be penetration testers to test and improve the security of networks or some
devices connected to these networks. It is capable of intercepting traffic on a network
segment, capturing passwords, and conducting active eavesdropping against a number of
common protocols.
* **Kali Linux** is a Debian-based Linux distribution. It is a meticulously crafted OS that
specifically caters to the likes of network analysts & penetration testers. The presence of a
plethora of tools that come pre-installed with Kali transforms it into an ethical hacker’s
swiss-knife.
* **Scapy** is a packet manipulation tool for computer networks. It can forge or decode packets,
send them on the wire, capture them, and match requests and replies. It can also handle
tasks like scanning, tracerouting, probing, unit tests, attacks, and network discovery.
* **Wireshark** is a free and open-source packet analyzer. It is used for network
troubleshooting, analysis, software and communications protocol development, and
education.

**Hardware Requirements**

• Processor – CORE i5 (3.0GHZ) or higher
• RAM – Above 4 GB
• Monitor

**Software Requirement**

• Operating system – Kali linux(Attacker machine) ,Ubuntu or windows (Victim machine)
• Tool – Scapy and wireshark
• Libraries – Scapy, Netifaces, nmap scan

# Modules

**ARP spoofing** module is a low-level process that translates the MAC to the IP address on
the local network.This module updates arp table on victim machine with forged response.

<p align="center">
    <img src="https://user-images.githubusercontent.com/71170862/127443874-15052b43-0d39-400f-a55e-782208d17d26.png" alt="ARP">
</p>

* INPUT : Target_IP and Gateway_IP
* PROCESS : arpspoof tool sends out forged response
* OUPUT : arptable on both the devices will be updated with forged response.

**DNS spoofing** module is where an attacker gives us a fake DNS entry that leads to a
different website.

<p align="center">
    <img src="https://user-images.githubusercontent.com/71170862/127443907-add5b8b9-8181-4c62-8ce3-a1115cef477e.png" alt="DNS">
</p>


* INPUT : Domain name of website
* PROCESS : Altered DNS records are used to redirect online traffic to a fraudulent website that resembles its intended destination
* OUTPUT : Victim will be redirected to fake website

**ARP detection** is a python script used to detect the arp spoof attack.

* INPUT : Arp packet
* PROCESS : The program will detect if any kind of packets has a layer of spoofed ARP
* OUTPUT : Prompts a message for Victim if they are spoofed.
