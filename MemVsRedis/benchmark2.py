__author__ = 'ahsanul'

import redis
import time

def without_pipeline():
    r = redis.Redis('192.168.8.88')
    for i in range(100000):
        r.set('i',i)
    return

def with_pipeline():
    r = redis.Redis()
    pipeline = r.pipeline()
    for i in range(100000):
        pipeline.set('i',i)
    pipeline.execute()
    return

def bench(method):
    start = time.clock()
    method()
    stop = time.clock()
    diff = stop - start
    print "time taken ",diff, " seconds"


if __name__ == "__main__":
    bench(without_pipeline)
    bench(with_pipeline)