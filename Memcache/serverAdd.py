__author__ = 'ahsanul'


import memcache,random,string,time

class MemcacheClient(memcache.Client):

    def _get_server(self, key):
        return super(MemcacheClient, self)._get_server(key)

    def add_server(self, server=None):
        if server is None:
            server = memcache._Host(
                server, self.debug, dead_retry=self.dead_retry,
                socket_timeout=self.socket_timeout,
            )

            self.servers.append(server)
            self.buckets.append(server)


def random_key(size):
    """ Generates a random key
    """
    return ''.join(random.choice(string.letters) for _ in range(size))

if __name__ == '__main__':

    # We have 7 running memcached servers
    servers = ["192.168.8.88:11211"]
    client = MemcacheClient(servers=servers)
    for i in range(-30,0):
        client.delete(str(i))
    client.add_server("192.168.122.186:11211")
    for i in range(-30,0):
        client.set(str(i), i)
        time.sleep(1)



