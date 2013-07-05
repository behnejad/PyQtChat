from threading import *
class hooman(Thread):
    def hooman(self):
        print "salam"
    def __init__(self):
        print "hooman has been run"
"""    
print "active_count()",active_count()
print "activeCount()",activeCount()
print "Condition()",Condition()
print "current_thread()",current_thread()
print "currentThread()",currentThread()
print "enumerate()",enumerate()
print "Event()",Event()
print "local()",local()
print "Lock()",Lock()
print "RLock()",RLock()
print "Class Threadin,","Class Timer"
"""
#settrace(hooman)
#hooman.start()
t = Thread(target = hooman())
