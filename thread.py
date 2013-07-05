import threading

class mythread (threading.Thread):
    def __init__ (self,name):
        threading.Thread.__init__(self)
        self.tname = name
        
    def run(self):
        for i in range(5):
            print ("Thread %s salam %d %s\n"%(self.tname,i,"kuft"))

a = mythread("salam")
b = mythread("shalgham")

a.start()
b.start()
