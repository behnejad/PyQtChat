__author__ = "Hooman Behnejad"
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def __recv__(c, cn, coName):
    global clientName
    global client
    while True:
        data = c.recv(1024)
        for i in range(len(clientName)):
            if clientName[i] == coName:
                coWorker = client[i]
                
        if data == "@@@bye!!!":
            break
        
        elif data:
            coWorker.send("%s@%s" % (cn, str(data)))

def __set__():
    global s
    global client
    global clientName
    s.listen(1)
    while True:
        c, address = s.accept()
        client.append(c)
        data = client[-1].recv(1024)
        data = data.split(":")
        if data[0] == ">-<":
            clientName.append(data[1])
            c.send("server@connected")
            threadList.append(Thread(target=__recv__, args=(c, clientName[-1], data[2])).start())



client = []
clientName = []
threadList = []

s = socket(family=AF_INET, type=SOCK_STREAM)
server_address = (str(raw_input("server address: ")), int(raw_input("server port: ")))
s.bind(server_address)
thread_set = Thread(target = __set__).start()

