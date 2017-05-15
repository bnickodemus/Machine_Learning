#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
from collections import Counter

# data.csv:
# dog,86,yes
# dog,75,no
# dog,30,yes
# cat,9,no
# cat,8,no
# cat,6,yes
# goat,57,no
# goat,3,yes
# goat,90,yes

#note the use of arguments dtype= and usecols=
animals = np.genfromtxt('data.csv', delimiter=',', dtype=None, usecols=(0))
nums = np.genfromtxt('data.csv', delimiter=',', usecols=(1))
yes_no = np.genfromtxt('data.csv', delimiter=',', dtype=None, usecols=(2))

#use np.unique to get options for each category
print np.unique(animals)
print np.unique(yes_no)

#how many "dog" animals were "true"
#use np.char.equal to find index of 'dog' in animals
i1 = np.char.equal(animals,'cat')
i2 = np.char.equal(animals,'no')

#use logical_and to find intersection of indices :
index = np.logical_and(i1,i2)
print np.mean(nums[index])
