__author__ = 'ahsanul'

''' Without cas(compare and set) we will face
 several race conditions'''
import memcache

def init_counter(mc,key):
    mc.set(key,0)


def inc_counter(mc, key):
    counter = mc.get(key)
    assert counter is not None,"Not initialized"
    mc.set(key,counter + 1)

def inc_counter_cas(mc,key):
    while True:
        counter = mc.gets(key)
        assert counter is not None,"Not initialized"
        if mc.cas(key,counter + 1):
            break

if __name__ == "__main__":
    mc = memcache.Client(["192.168.8.88:11211"])
    init_counter(mc,"incr")
    inc_counter(mc,"incr")