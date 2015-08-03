__author__ = 'ahsanul'

import memcache,time,sys


def operationToIndivisual(timeInSeconds):
    mc = memcache.Client(["192.168.8.88:11211"])
    time.sleep(4.7)
    print "start"
    time.sleep(timeInSeconds-5)
    print "Final Start"
    for i in range(200000):
        mc.incr('memMulti')
    print mc.get('memMulti')
    return timeInSeconds


def bench(method,seconds):
    start = time.clock()
    method(seconds)
    stop = time.clock()
    diff = stop - start
    print "time taken ",diff, " seconds"


if __name__ == "__main__":
    bench(operationToIndivisual,int(sys.argv[1]))
