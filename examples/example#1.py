#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# generate N x M matrix (N>=10)
M = 3
N = 100
data = np.random.randint(0,10,(N,M))

# plot each column one at a time
for m in range(M):
    plt.subplot(M,1,m+1)
    plt.plot(data[:,m])

plt.show()

# gen some stats on each row
for n in range(N):
    x = np.mean(data[n,:])
    print x

# find entries >= k, some value
k = 4
i = data >= k
plt.plot(data[i],'*')

#r,c=np.shape(data)
