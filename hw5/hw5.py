import numpy as np
from sklearn import linear_model

# read in testing data
mpg = np.genfromtxt('auto-mpg-test.data', delimiter=' ', dtype=None, usecols=(0))
cylinders = np.genfromtxt('auto-mpg-test.data', delimiter=' ', dtype=None, usecols=(1))
displacement = np.genfromtxt('auto-mpg-test.data', delimiter=' ', dtype=None, usecols=(2))
horsepower = np.genfromtxt('auto-mpg-test.data', delimiter=' ', dtype=None, usecols=(3))
weight = np.genfromtxt('auto-mpg-test.data', delimiter=' ', dtype=None, usecols=(4))
acceleration = np.genfromtxt('auto-mpg-test.data', delimiter=' ', dtype=None, usecols=(5))
model_year = np.genfromtxt('auto-mpg-test.data', delimiter=' ', dtype=None, usecols=(6))
origin = np.genfromtxt('auto-mpg-test.data', delimiter=' ', dtype=None, usecols=(7))
car_name = np.genfromtxt('auto-mpg-test.data', delimiter=' ', dtype=None, usecols=(8))
 
#my_data = np.genfromtxt('auto-mpg-test.data', delimiter=' ')
#filter(None, my_data)

# filter out options
filter(None, weight) 
filter(None, mpg)
filter(None, cylinders)
filter(None, displacement)
filter(None, horsepower)

# this didnt work
#arr = np.column_stack((cylinders, displacement, horsepower, weight))
#y = mpg
#x = my_data
#X = np.column_stack(x+[[1]*len(x[0])])
#beta_hat = np.linalg.lstsq(X,y)[0]
#print np.dot(X,beta_hat)

# fit linear regession
regr = linear_model.LinearRegression()
regr.fit(weight.reshape(len(weight), 1), mpg)

# predict the mpg based on the weight
ndArry = regr.predict(weight.reshape(len(weight), 1))

#combine columns & save to csv
ndArry = np.column_stack([mpg, ndArry])
np.savetxt('nickodemus.csv', ndArry, fmt='%1.4f', delimiter=',')