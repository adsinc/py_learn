import shelve

from Preview.initdata import bob, sue

db = shelve.open('tmp/people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
