import shelve

fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('tmp/class-shelve')

while True:
    key = input('\Key? => ')
    if not key:
        break

    try:
        record = db[key]
    except KeyError:
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))
