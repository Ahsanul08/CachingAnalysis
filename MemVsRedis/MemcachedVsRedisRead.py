__author__ = 'ahsanul'

import redis,memcache
import time

def memcached():
    mc = memcache.Client(["192.168.8.88:11211"])
    for i in range(100000):
        mc.get('i')
    return

def without_pipeline():
    r = redis.Redis('192.168.8.88')
    for i in range(100000):
        r.get('i')
    return

def with_pipeline():
    r = redis.Redis()
    pipeline = r.pipeline()
    for i in range(100000):
        pipeline.get('i')
    pipeline.execute()
    return

def bench(method):
    start = time.clock()
    method()
    stop = time.clock()
    diff = stop - start
    print "time taken ",diff, " seconds"


if __name__ == "__main__":
    bench(memcached)
    bench(without_pipeline)
    bench(with_pipeline)

