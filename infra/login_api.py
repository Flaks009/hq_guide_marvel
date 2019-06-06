import hashlib
from time import time

ts = str(time())
api_key = '0e2daa8082215ef226a926ff5e8a45d3'
pk = 'd5094fcb2928321006e79504263d1823cdb95af4'

def key(ts, api_key, pk):
    return (hashlib.md5((ts+pk+api_key).encode('utf-8')).hexdigest())

hash_key = key(ts, api_key, pk)