import threading
from time import ctime,sleep

loops = [4,2]

class mythread(threading.Thread):
    """docstring for mythread"""
    def __init__(self, func, args, name = ''):
        threading.Thread.__init__(slef)
        self.arg = args
        self.name = name
        self.func = func

    def run(self):
        apply(self.func,self.args)
    
def loop(nloop,nesc):
    print "start loop",nloop,"at:",ctime()
    sleep(nesc)
    print "loop",nloop,"done at:",ctime()


def main():
    print "start at:",ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = mythread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)


    for i in nloops:
        threads[i].start()

    for i in nloops:
        threading[i].join()

    print "all dine at:",ctime()


if __name__ == '__main__':
    main()