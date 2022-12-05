#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[91m
    _____ ___ ___ __  __ _   ___  __  ___  _   ___ _  __   _   ___ ___ 
  |_   _| __| _ \  \/  | | | \ \/ / | _ \/_\ / __| |/ /  /_\ / __| __|
    | | | _||   / |\/| | |_| |>  <  |  _/ _ \ (__| ' <  / _ \ (_ | _| 
    |_| |___|_|_\_|  |_|\___//_/\_\ |_|/_/ \_\___|_|\_\/_/ \_\___|___|                                                                       
                                                                                                                                                                                                                              
INSPIRED BY  poisk-ls
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[95m
+---------------------------------------+
| This Script Install All Basic Packages |
+---------------------------------------+
| Inspired by poisk-ls |  version : 2.3  |
+---------------------------------------+''')

slowprint(''' \033[93m
[01] python
[02] python2
[03] python-dev
[04] python3
[05] php
[06] java
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] openssl
[13] openssh
[14] wget
[15] clang
[16] nmap
[17] w3m
[18] hydra
[19] ruby
[20] macchanger
[21] host
[22] dnsutils
[23] coreutils
[24] fish
[25] zip
[27] tor
[28] hydra
[29] figlet 
[30] cowsay
[31] tar
[32] unzip
[33] vim
[34] ruby
[35] wcalc
[36] bmon
[37] unrar
[38] proot
[39] nano
[40] golang
[41] clang''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")
os.system ("pkg upgrade -y")
os.system ("pkg install python -y")
os.system ("pkg install python2 -y")
os.system ("pkg install php -y")
os.system ("pkg install python-dev -y")
os.system ("pkg install python3 -y")
os.system ("pkg install java -y")
os.system ("pkg install git -y")
os.system ("pkg install perl -y")
os.system ("pkg install bash")

print ("wait for second and start hacking")

os.system ("pkg install nano -y")
os.system ("pkg install curl -y")
os.system ("pkg install openssl -y")
os.system ("pkg install openssh -y")
os.system ("pkg install wget -y")
os.system ("pkg install clang -y")
os.system ("pkg install nmap -y")
os.system ("pkg install w3m -y")
os.system ("pkg install hydra -y")


print ("""
Inspired by: poisk-ls""")

os.system ("pkg install ruby -y")
os.system ("pkg install macchanger -y")
os.system ("pkg install host -y")
os.system ("pkg install dnsutils -y")
os.system ("pkg install coreutils -y")
os.system ("pkg install fish -y")
os.system ("pkg install zip -y")
os.system ("pkg install hydra -y")
os.system ("pkg install figlet -y")
os.system ("pkg install cowsay -y")
os.system ("pkg install unzip -y")
os.system ("pkg install vim -y")
os.system ("pkg install ruby -y")
os.system ("pkg install wcalc -y")
os.system ("pkg install bmon -y")
os.system ("pkg install unrar -y")
os.system ("pkg install proot -y")
os.system ("pkg install golang -y")
os.system ("pkg install clang -y")
print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")
  
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|         Welcome To poisk-ls            |
| Don't forget to follow me on Github  |''')
print("+-------------------------------------------------+")


input("\n\nPress the enter key to exit : ")
