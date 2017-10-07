import pickle
suefile = open('tmp/sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()
sue['pay'] *= 1.10
suefile = open('tmp/sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()
