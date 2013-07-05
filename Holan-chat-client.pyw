from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys, socket, threading

class widget(QDialog):
    def __init__ (self, patern = None):
        QDialog.__init__(self, patern)
        self.client_name = self.getName()
        #close event is not suitble
        self.center()
        self.setWindowTitle("****PyQt CHAT client****")

        grid = QGridLayout(self)

        name = QLabel("Welcome to our chat, your name will be <" + self.client_name + \
                            ">.\nplease select one of these person and click talk")
        grid.addWidget(name, 0, 0, 1, 1)

        clients = QListWidget(self)
        grid.addWidget(clients, 1, 0, 2, 2)

        talk = QPushButton("Talk")
        grid.addWidget(talk, 4, 0, 1, 1)

        visible = QCheckBox("make me invisible")
        grid.addWidget(visible, 4, 1, 1, 1)


        for i in range(20):
            clients.addItem(str(i+1))





    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit-Message',"Are you sure to quit?",
                                                QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.resize(200,200)
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def getName(self):
        text, ok = QInputDialog.getText(self, '**PyQt CHAT**', 'What is yourname?')
        if ok:
            return unicode(text)
        else:
            self.close()
            return False

class chat(QDialog):
    def __init__ (self, patern = None):
        QDialog.__init__(self, patern)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = widget()
    a.show()
    sys.exit(app.exec_())