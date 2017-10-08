import shelve
db = shelve.open('tmp/people-shelve')
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])
db.close()
