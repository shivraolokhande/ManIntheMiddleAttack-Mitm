#!/usr/bin/env python

import scapy.all as scapy

def mac(ipadd):
    arp_request = scapy.ARP(pdst=ipadd)
    br = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_br = br / arp_request
    list_1 = scapy.srp(arp_req_br, timeout=5, verbose=False)[0]
    return list_1[0][1].hwsrc

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
         originalmac = mac(packet[scapy.ARP].psrc)
         responsemac = packet[scapy.ARP].hwsrc

         if originalmac != responsemac:
             print("[*] ALERT!! You are under attack, the ARP table is being poisoned.!")

interface = input("Enter the interface > ")


sniff(interface)
