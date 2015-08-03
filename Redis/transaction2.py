__author__ = 'ahsanul'

import redis,time

r = redis.Redis("192.168.8.88")
var = r.get("transError")
var = int(var) + 1
r.set("transError",int(var)+1)

print "Value in second Client",r.get("transError")
