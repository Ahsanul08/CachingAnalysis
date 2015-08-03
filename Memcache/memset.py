__author__ = 'ahsanul'

import memcache

mc = memcache.Client(["192.168.8.88:11211"])
print mc.set('memMulti',0)