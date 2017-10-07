import pickle
import glob

for filename in glob.glob('tmp/*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n', record)

suefile = open('tmp/sue.pkl', 'rb')
print(pickle.load(suefile)['name'])
