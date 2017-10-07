import pickle

from Preview.initdata import bob, sue, tom

for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open('tmp/' + key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()
