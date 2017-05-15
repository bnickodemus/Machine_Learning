import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn import neighbors

# read in training data
varience = np.genfromtxt('banknote_train.csv', delimiter=',', dtype=None, usecols=(0))
skewness = np.genfromtxt('banknote_train.csv', delimiter=',', dtype=None, usecols=(1))
curtosis = np.genfromtxt('banknote_train.csv', delimiter=',', dtype=None, usecols=(2))
entropy = np.genfromtxt('banknote_train.csv', delimiter=',', dtype=None, usecols=(3))
label = np.genfromtxt('banknote_train.csv', delimiter=',', dtype=None, usecols=(4))

# combine columns
ndArry = np.column_stack((varience, skewness, curtosis, entropy))

nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(ndArry)
distances, indices = nbrs.kneighbors(ndArry)

# create classifier
clf = neighbors.KNeighborsClassifier(n_neighbors=5, weights=weights)
clf.fit(ndArry, label)
    
Y = clf.predict(ndArry)
print Y

# append the predicted column
ndArry = np.column_stack((ndArry, Y))

# output the data and label
np.savetxt('nickodemus.csv', ndArry, fmt='%1.4f', delimiter=',')
