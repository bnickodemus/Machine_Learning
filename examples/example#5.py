import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Flatten

from keras import backend as k
k.set_image_dim_ordering('th')

np.random.seed(2)

(X,y),(Xp,yp) = mnist.load_data()
X2 = X
num_pixels = X.shape[1] * X.shape[2]
X = X.reshape(X.shape[0],1,28,28).astype('float32')
Xp = Xp.reshape(Xp.shape[0],1,28,28).astype('float32')

X /= 255.0
Xp /= 255.0

y = np_utils.to_categorical(y)
yp = np_utils.to_categorical(yp)
num_classes = y.shape[1]

# add another convoution 2d layer
# add another pooling layer
# add another hidden layer

def cnn_model():
    model = Sequential()
    model.add(Convolution2D(32,5,5,border_mode='valid',input_shape=(1,28,28),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128,activation='relu'))
    model.add(Dense(num_classes,activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    return model

cnn= cnn_model()
cnn.fit(X,y, batch_size=200, nb_epoch=10, verbose=2, validation_data=(Xp,yp))
scores = cnn.evaluate(Xp,yp)

print ((100-scores[1])*100)
