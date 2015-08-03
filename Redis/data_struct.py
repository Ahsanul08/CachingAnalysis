__author__ = 'ahsanul'

import redis
r = redis.Redis('192.168.8.88')

#string
print r.set("name","ovi")
print r.get("name")

r.rpop("greeting")
r.lpop("greeting")
#list operations
r.rpush("greeting","hello")
r.lpush("greeting","hi")

print "Length of the list is: ", r.llen("greeting")
print "Elements of the list is:", r.lrange("greeting",0,1)

#hashes

r.hset("hashes","name","omi")
print r.hkeys("hashes")
print r.hvals("hashes")

#set
r.sadd("sets1","ovi")
r.sadd("sets1","omi")
r.sadd("sets2","omi")
r.sadd("sets2","ovi")

print r.sunion("sets1","sets2")
print r.sinter("sets1","sets2")

#sorted sets
r.zadd("sset1","ghanima",100)
r.zadd("sset1","duncan",994)
r.zadd("sset1","dano",93)

print r.zrangebyscore("sset1",0,500)

