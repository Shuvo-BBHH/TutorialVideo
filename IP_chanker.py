# TO day i show you how to finad any wabsite ip address using python
# le's Start
import socket # this is modul fo ip chack: must install 'pip install socket'
import mahdix # This is my modul for use coloure: must install 'pip install mahdix'
GREEN = mahdix.LI_GREEN
YELLOW =mahdix.LI_YELLOW
RED = mahdix.LI_RED
wabsite=input(f"{GREEN} INPUT WABSITE NAME : ")
getip = socket.gethostbyname(wabsite)  # THIS IS MAIN FUNcting

print(f'{YELLOW}Your wabsite is : {wabsite}')
print(f'{GREEN}you wb ip is : {RED}{getip}')
# DONE
