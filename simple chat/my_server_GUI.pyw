__author__ = 'Hooman'

from threading import Thread
from PyQt4 import QtGui, QtCore
from sys import exit, argv
from socket import socket, AF_INET, SOCK_STREAM

class UI(QtGui.QDialog):
    def __init__(self, size):
        QtGui.QWidget.__init__(self, None)
        self.resize(size[0], size[1])
        self.setWindowTitle("simple chat server")
        self.clientName = []
        self.client = []
        self.threadList = []
        self.__creat__()
        self.__connect__()

    def __creat__(self):
        self.grid = QtGui.QGridLayout(self)

        self.hostAddr = QtGui.QLabel(self)
        self.hostAddr.setText("Host Address:")
        self.grid.addWidget(self.hostAddr, 0, 0, 1, 1)

        self.getHostAddr = QtGui.QLineEdit(self)
        self.grid.addWidget(self.getHostAddr, 0, 1, 1, 1)

        self.hostPort = QtGui.QLabel(self)
        self.hostPort.setText("Host Port:")
        self.grid.addWidget(self.hostPort, 0, 2, 1, 1)

        self.getHostPort = QtGui.QLineEdit(self)
        self.grid.addWidget(self.getHostPort, 0, 3, 1, 1)

        self.receive_list = QtGui.QListWidget(self)
        self.grid.addWidget(self.receive_list, 1, 0, 4, 4)

        self.send_text = QtGui.QLineEdit(self)
        self.grid.addWidget(self.send_text, 5, 0, 4, 4)

        self.sendButton = QtGui.QPushButton(self)
        self.sendButton.setText("send")
        self.grid.addWidget(self.sendButton, 9, 0, 1, 2)

        self.conButton = QtGui.QPushButton(self)
        self.conButton.setText("Connect")
        self.grid.addWidget(self.conButton, 9, 2, 1, 1)

        self.disButton = QtGui.QPushButton(self)
        self.disButton.setText("Disconnect")
        self.grid.addWidget(self.disButton, 9, 3, 1, 1)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Quit-Message',
                                     "Are you sure you want to quit?",
                                     QtGui.QMessageBox.No,
                                     QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def __connect__(self):
        self.connect(self.sendButton, QtCore.SIGNAL('clicked()'), self.__send__)
        self.connect(self.conButton, QtCore.SIGNAL('clicked()'), self.__conSocket__)
        self.connect(self.disButton, QtCore.SIGNAL('clicked()'), self.__disconSocket__)

    def __send__(self):
        if str(self.send_text.text()) != "":
            for client in self.client:
                client.send(str(self.send_text.text()))
            self.receive_list.addItem("%s: %s" % ("server", self.send_text.text()))
            self.send_text.clear()
       
    def __recv__(self, client, clientName):
        while True:
            data = client.recv(1024)
            if data:
                 self.receive_list.addItem("%s: %s" % (clientName, data))
        
    def __conSocket__(self):
        self.receive_list.addItem("connecting")
        self.socket = socket(family=AF_INET, type=SOCK_STREAM)
        self.server_address = (str(self.getHostAddr.text()) ,int(self.getHostPort.text()))
        self.socket.bind(self.server_address)
        
        self.thread_set = Thread(target = self.__set__).start()
        
        self.getHostPort.setDisabled(True)
        self.conButton.setDisabled(True)
        self.getHostAddr.setDisabled(True)

    def __set__(self):
        self.socket.listen(1)
        while True:
            client, address = self.socket.accept()
            self.client.append(client)
            data = self.client[-1].recv(1024)
            if data[:3] == ">-<":
                self.clientName.append(data[3:])
                self.receive_list.addItem("%s connected" % self.clientName[-1])
                self.threadList.append(Thread(target=self.__recv__, args=(client, self.clientName[-1])).start())
        
    def __disconSocket__(self):
        self.socket.close()
        del self.socket
        self.getHostPort.setDisabled(False)
        self.conButton.setDisabled(False)
        self.getHostAddr.setDisabled(False)


if __name__ == "__main__":
    app = QtGui.QApplication(argv)
    size = width, height = (400, 300)
    w = UI(size)
    w.show()
    exit(app.exec_())
