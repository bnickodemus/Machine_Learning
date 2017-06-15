import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Flatten

np.random.seed(2)

(X,y),(Xp,yp) = mnist.load_data()
X2 = X
num_pixels = X.shape[1] * X.shape[2]
X = X.reshape(X.shape[0],num_pixels).astype('float32')
Xp = Xp.reshape(Xp.shape[0],num_pixels).astype('float32')

X /= 255.0
Xp /= 255.0

p = y
y = np_utils.to_categorical(y)
yp = np_utils.to_categorical(yp)
num_classes = y.shape[1]

def MLP_model():
    model = Sequential()
    model.add(Dense(10, input_dim=num_pixels, init='normal', activation='relu'))
    model.add(Dense(5, init='normal', activation='relu'))
    model.add(Dense(num_classes, init='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    return model
'''
mlp = MLP_model()
mlp.fit(X,y,validation_data=(Xp,yp), nb_epoch=10, batch_size=200, verbose=2)
scores = mlp.evaluate(Xp,yp,verbose=0)
print 'MLP error %.2f%%' % ((100-scores[1])*100)
'''