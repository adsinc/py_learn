import shelve
db = shelve.open('tmp/class-shelve')
for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)

bob = db['bob']
print(bob.last_name())
print(db['tom'].last_name())
