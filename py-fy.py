#!/usr/bin/env python3

"""
import os -> subprocess is better since it does not spawn a direct shell
process, rather it executes the command directly, which makes more efficient!

Opt out of using (os) library....
"""
import sys
import subprocess
import re
from time import sleep



ascii = """

 ________  ___    ___             ________ ___    ___
|\   __  \|\  \  /  /|           |\  _____\\  \  /  /|
\ \  \|\  \ \  \/  / /___________\ \  \__/\ \  \/  / /
 \ \   ____\ \    / /\____________\ \   __\\ \    / /
  \ \  \___|\/  /  /\|____________|\ \  \_| \/  /  /
   \ \__\ __/  / /                  \ \__\__/  / /
    \|__||\___/ /                    \|__|\___/ /
         \|___|/                         \|___|/

-> With <3 by A.Vlasto (@vish) && K.Karabadzhakov (@Kr0ff)
"""

print(ascii)


adapter = ""

def find_adapter():
    print("[+] Checking available network adapters...")
    try:
        ip_addr = subprocess.call(["/usr/sbin/ip", "addr"])
    except:
        print("[-] Command not found !")
        sleep(1)
        return menu()

def airodump(): #airodump-ng
    selection = """
    (1) - Capture packets from all APs
    (2) - Capture packets from specific channel and AP
    """
    channel = ''

    print(selection)
    option = input("Select option: ")

    if option == "1":
        print("[+] Capturing packets from all APs")
        all_APs = subprocess.call(["/usr/sbin/airodump-ng", "{}"]).format(adapter)
        print(all_APs)

    elif option == "2":
        select_channel = input("Select channel to capture from: ").format(channel)
        specific_Channel = subprocess.call(["/usr/sbin/airodump-ng", "--channel {}", "{}"]).format(select_channel, adapter)
        print(specific_Channel)
        print("[+] Packet capture started...")

    else:
        print("[-] Sry no such option")
        return airodump()

if __name__ == "__main__": #BEGIN

#That's the menu :)
    def menu():

        menu = """
        (0) Find NetAdapter and start Monitor Mode
        (1) Capture packets via (airodump-ng)
        ...
        """

        print(menu)
        option = input("[*] Select option: ")

        if option == "0":
            find_adapter()

        elif option == "1":
            airodump()

        else:
            print("[-] Selected option not found !")
            menu()


menu()
