import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn import neighbors

# load data
white = np.loadtxt('wine-quality-white-train.csv', delimiter=';', skiprows=1, dtype=None)
red = np.loadtxt('wine-quality-red-train.csv', delimiter=';', skiprows=1, dtype=None)
test = np.loadtxt('wine-quality-test.csv', delimiter=';', skiprows=1, dtype=None)
idcol = test[:,0]
train = np.concatenate((white,red))

# initialize PCA and classifier
# pca = PCA() # using all columns didnt work
pca = PCA(n_components=3)
classifier = DecisionTreeClassifier()

cat = train.astype(int, order='K', casting='unsafe', subok=True, copy=True)

# run the PCA on all the attributes 
X_transformed = pca.fit_transform(cat)

classifier.fit(X_transformed, cat[:,11])

# cumulative variance
var1 = np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)
print var1
plt.plot(var1)

# looking at above plot above, I'm going to use 3 vaiables
pca = PCA(n_components=3)
#pca.fit(cat)
pca.fit_transform(cat)

# predict new data
newdata = test.astype(int, order='K', casting='unsafe', subok=True, copy=True)

# transform new data using already fitted pca
newdata_transformed = pca.transform(newdata)
pred_quality = classifier.predict(newdata_transformed)

# append a column of 0's to red and 1's to white
red = np.column_stack((red,np.zeros((len(red)))))
white = np.column_stack((white,np.ones((len(white)))))
train = np.concatenate((white,red))
label = train[:,12]

# claculate k nearest 
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(train)
distances, indices = nbrs.kneighbors(train)
clf = neighbors.KNeighborsClassifier(n_neighbors=5)
clf.fit(train, label)

# append col of -1 to test data
badcol = np.ndarray(shape=(len(test),1))
for i in range(len(test)):
    badcol[i] = -1    

test = np.column_stack((test,badcol)) 
redOrWhite = clf.predict(test) # we cannot predict unless there is another column  :(

# store columns in output for printing
output = np.column_stack((idcol,pred_quality))
output = np.column_stack((output,redOrWhite))

# save to csv
np.savetxt('nickodemus.csv', output, fmt='%1.4f', delimiter=',')
