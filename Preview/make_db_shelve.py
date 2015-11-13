import shelve

from Preview.initdata import bob, sue

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
