__author__ = 'ahsanul'

import redis,time

r = redis.Redis("192.168.8.88")
r.set("transError",10)
var = r.get("transError")
print "Run other client to simulate an error without transaction"
time.sleep(4)
r.set("transError",int(var)+1)
print "Value in first client",r.get("transError")