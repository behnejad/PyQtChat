import threading

def worker():
    """thread worker function"""
    print 'Worker\n'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
print threads
