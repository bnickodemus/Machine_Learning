import numpy as np
from keras.models import Sequential
from keras.layers import Dense
np.random.seed(2)

# load in the data
train = np.loadtxt('semeion-train.data')
test = np.loadtxt('semeion-test.data')
index = np.genfromtxt('semeion-test.data', delimiter=' ', usecols=(0))

# use only the columns we need
X = train[:,0:256]
y = train[:,256:]
Xp = test[:,1:257]

# define MLP and attributes 
def MLP_model():
    model = Sequential()
    model.add(Dense(100, input_dim=256, init='normal', activation='relu'))
    model.add(Dense(10, init='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    return model

# create MLP
mlp = MLP_model()
mlp.fit(X,y, nb_epoch=10, batch_size=200, verbose=2)
predict = mlp.predict(Xp)

# predict based on the the max value
pred = predict.argmax(axis=1)
output = np.column_stack((index,pred))

# print output
np.savetxt('nickodemus.csv', output, fmt='%1f', delimiter=',')
