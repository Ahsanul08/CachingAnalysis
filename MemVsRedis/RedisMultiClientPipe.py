__author__ = 'ahsanul'


import redis,memcache
import time,sys


def with_pipeline(timeInSeconds):
    r = redis.Redis()
    pipeline = r.pipeline()
    time.sleep(4.7)
    print 'start'
    time.sleep(timeInSeconds-5)
    print "Final Start"
    for i in range(200000):
        pipeline.incr('redMulti')
    pipeline.execute()
    print pipeline.get('redMulti')
    return

def bench(method,seconds):
    start = time.clock()
    method(seconds)
    stop = time.clock()
    diff = stop - start
    print "time taken ",diff, " seconds"


if __name__ == "__main__":
    bench(with_pipeline,int(sys.argv[1]))


