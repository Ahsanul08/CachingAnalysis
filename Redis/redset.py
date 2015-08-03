__author__ = 'ahsanul'

import redis

r = redis.Redis()
print r.set('redMulti',0)