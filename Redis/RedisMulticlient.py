__author__ = 'ahsanul'


import redis,memcache
import time,sys


def without_pipeline(timeInSeconds):
    r = redis.Redis()
    time.sleep(4.7)
    print 'start'
    time.sleep(timeInSeconds-5)
    print "Final Start"
    for i in range(200000):
        r.incr('redMulti')
    print r.get('redMulti')
    return

def bench(method,seconds):
    start = time.clock()
    method(seconds)
    stop = time.clock()
    diff = stop - start
    print "time taken ",diff, " seconds"


if __name__ == "__main__":
    bench(without_pipeline,int(sys.argv[1]))


