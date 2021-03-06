import shelve
from Preview.person import Person
fieldnames = ('name', 'age', 'job', 'pay')

db = shelve.open('tmp/class-shelve')

while True:
    key = input('\Key? => ')
    if not key:
        break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        curval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, curval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()
