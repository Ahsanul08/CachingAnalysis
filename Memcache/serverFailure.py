__author__ = 'ahsanul'

import memcache,time


def serverFailureTest():
    mc = memcache.Client(["192.168.8.88:11211","192.168.122.223:11211","192.168.122.186:11211"])
    for i in range(100000):
        mc.delete(str(i))
    print "Preparing"
    time.sleep(2)
    print "Time to set value:"
    for i in range(100000):
        mc.set(str(i),i)
    print "Stop a Server within 5 sec to simulate a server failure"
    time.sleep(5)
    dataloss = 0
    for i in range(100000):
        value = mc.get(str(i))
        print value
        if not value:
            store = str(i)
            dataloss = dataloss + 1
    print "In total ", dataloss , " no. of data can't be fetched"
    print store

if __name__ == "__main__":
    serverFailureTest()
