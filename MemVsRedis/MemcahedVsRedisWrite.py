__author__ = 'ahsanul'

import redis,memcache
import time

def memcached():
    mc = memcache.Client(["192.168.8.88:11211"])
    for i in range(200000):
        mc.set('i',i)
    return

def without_pipeline():
    r = redis.Redis('192.168.8.88')
    for i in range(200000):
        r.set('i',i)
    return

def with_pipeline():
    r = redis.Redis()
    pipeline = r.pipeline()
    for i in range(200000):
        pipeline.set('i',i)
    pipeline.execute()
    return

def bench(method):
    start = time.clock()
    method()
    stop = time.clock()
    diff = stop - start
    print "time taken by ",method," ",diff, " seconds"


if __name__ == "__main__":
    bench(without_pipeline)
    bench(memcached)

    bench(with_pipeline)


