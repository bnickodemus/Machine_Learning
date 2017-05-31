import numpy as np

train = np.loadtxt('semeion-train.data')
X = train[:,0:256]
Y = train[:,256:266]

myList = []

for i in Y: # for row in column
    #print i
    if i[0] == 1:
        myList.append(0)
    if i[1] == 1:
        myList.append(1)
    if i[2] == 1:
        myList.append(2)
    if i[3] == 1:
        myList.append(3)
    if i[4] == 1:
        myList.append(4)
    if i[5] == 1:
        myList.append(5)
    if i[6] == 1:
        myList.append(6)
    if i[7] == 1:
        myList.append(7)
    if i[8] == 1:
        myList.append(8)
    if i[9] == 1:
        myList.append(9)
    
output = np.column_stack((X,myList))    
    
np.savetxt('output.csv', output, fmt='%1.0f', delimiter=',')