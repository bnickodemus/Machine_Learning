#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random as rdm
import numpy as np

data = [ x**2 for x in range(100)]

plt.plot(data)
plt.xlabel('x')
plt.ylabel('x**2')
plt.title('TITLE')
plt.show()

#five x and y values
plt.figure()
plt.plot(range(5), data[:5], 'g^') # x: 0-99 y: x^2  # g* ,g^
plt.show()

#histograms
data = [rdm.random() for _ in range(50)]
plt.hist(data)
plt.show()

data = np.random.normal(size=10000)
plt.hist(data,100)
plt.show()

#bar charts
x = range(10)
y = [rdm.random() for _ in x]
plt.bar(x,y) #bins and heights
plt.xticks(x,['Marc' + str(z) for z in x])
plt.show()

x1 = range(10)
x2 = range(10)
rdm.shuffle(x1)
rdm.shuffle(x2)
y1 = [rdm.random() for _ in x1]
y2 = [rdm.random() for _ in x2]
A = plt.scatter(x1,y1,color='g')
B = plt.scatter(x2,y2,color='r')
plt.axis([0,100,0,100]) # comment
plt.legend([A,B],['x1','x2'])
plt.show()
