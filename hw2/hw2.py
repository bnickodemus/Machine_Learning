import numpy as np
import matplotlib.pyplot as plt

par1x = np.genfromtxt('1.csv', delimiter=',', dtype=None, usecols=(1))
par1y = np.genfromtxt('1.csv', delimiter=',', dtype=None, usecols=(2))
par1z = np.genfromtxt('1.csv', delimiter=',', dtype=None, usecols=(3))
activity = np.genfromtxt('1.csv', delimiter=',', dtype=None, usecols=(4))

row = np.genfromtxt('1.csv', delimiter=',', dtype=None) 
activity = []
par1cpuX = []
par1cpuY = []
par1cpuZ = []
time = []

par1walkX = []
par1walkY = []
par1walkZ = []
walkTime = []
counter = 0

par1stairsX = []
par1stairsY = []
par1stairsZ = []
stairTime = []
stairCounter = 0

par1standX = []
par1standY = []
par1standZ = []
standTime = []
standCounter = 0

# get data row by row
for i in row:
    if i[4] == 1:
        time.append(i[0])
        par1cpuX.append(i[1])
        par1cpuY.append(i[2])
        par1cpuZ.append(i[3])
    if i[4] == 3:
        standCounter += 1
        standTime.append(standCounter)
        par1standX.append(i[1])
        par1standY.append(i[2])
        par1standZ.append(i[3])
    if i[4] == 4:
        counter += 1
        walkTime.append(counter)
        par1walkX.append(i[1])
        par1walkY.append(i[2])
        par1walkZ.append(i[3])
    if i[4] == 5:
        stairCounter += 1
        stairTime.append(stairCounter)
        par1stairsX.append(i[1])
        par1stairsY.append(i[2])
        par1stairsZ.append(i[3])
        
        
# graph 1
# blue cpu
time = [float(x / 52.0) for x in time] # / 52 hz
par1cpuX = np.array(par1cpuX) 
x = par1cpuX / float(np.max(np.absolute(par1cpuX)))        
par1cpuX = x - np.mean(x)

# green cpu
par1cpuY = np.array(par1cpuY)
y = par1cpuY / float(np.max(np.absolute(par1cpuY)))
par1cpuY = y - np.mean(y)
par1cpuY = par1cpuY + 0.2

# red cpu
par1cpuZ = np.array(par1cpuZ)
z = par1cpuZ / float(np.max(np.absolute(par1cpuZ)))
par1cpuZ = z - np.mean(z)
par1cpuZ = par1cpuZ - 0.2

# graph 2
# blue standing
standTime = [float(g / 52.0) for g in standTime]
par1standX = np.array(par1standX) 
x = par1standX / float(np.max(np.absolute(par1standX)))        
par1standX = x - np.mean(x)

# green standing
par1standY = np.array(par1standY)
y = par1standY / float(np.max(np.absolute(par1standY)))
par1standY = y - np.mean(y)
par1standY = par1standY + 0.2

# red standing
par1standZ = np.array(par1standZ)
y = par1standZ / float(np.max(np.absolute(par1standZ)))
par1standZ = y - np.mean(y)
par1standZ = par1standZ - 0.2

# graph 3
# blue walking
walkTime = [float(g2 / 52.0) for g2 in walkTime]
par1walkX = np.array(par1walkX) 
x = par1walkX / float(np.max(np.absolute(par1walkX)))        
par1walkX = x - np.mean(x)

# green walking
par1walkY = np.array(par1walkY)
y = par1walkY / float(np.max(np.absolute(par1walkY)))
par1walkY = y - np.mean(y)
par1walkY = par1walkY + 0.2

# red walking
par1walkZ = np.array(par1walkZ)
y = par1walkZ / float(np.max(np.absolute(par1walkZ)))
par1walkZ = y - np.mean(y)
par1walkZ = par1walkZ - 0.2

# graph 4
# blue stairs
stairTime = [float(g3 / 52.0) for g3 in stairTime]
par1stairsX = np.array(par1stairsX) 
x = par1stairsX / float(np.max(np.absolute(par1stairsX)))        
par1stairsX = x - np.mean(x)

# green stairs
par1stairsY = np.array(par1stairsY)
y = par1stairsY / float(np.max(np.absolute(par1stairsY)))
par1stairsY = y - np.mean(y)
par1stairsY = par1stairsY + 0.2

# red stairs
par1stairsZ = np.array(par1stairsZ)
y = par1stairsZ / float(np.max(np.absolute(par1stairsZ)))
par1stairsZ = y - np.mean(y)
par1stairsZ = par1stairsZ - 0.2

# Four axes, returned as a 2-d array
f, axarr = plt.subplots(2, 2)
axarr[0, 0].plot(time, par1cpuX, color='b')
axarr[0, 0].plot(time, par1cpuY, color='g')
axarr[0, 0].plot(time, par1cpuZ, color='r')
axarr[0, 0].set_title('Working at Computer')
axarr[0, 0].set_xlabel('time(s)')
axarr[0, 0].set_ylabel('normalized magnitude')

axarr[0, 1].plot(standTime, par1standX, color='b')
axarr[0, 1].plot(standTime, par1standY, color='g')
axarr[0, 1].plot(standTime, par1standZ, color='r')
axarr[0, 1].set_title('Standing')
axarr[0, 1].set_xlabel('time(s)')
axarr[0, 1].set_ylabel('normalized magnitude')

axarr[1, 0].plot(walkTime, par1walkX, color='b')
axarr[1, 0].plot(walkTime, par1walkY, color='g')
axarr[1, 0].plot(walkTime, par1walkZ, color='r')
axarr[1, 0].set_title('Walking')
axarr[1, 0].set_xlabel('time(s)')
axarr[1, 0].set_ylabel('normalized magnitude')

axarr[1, 1].plot(stairTime, par1stairsX, color='b')
axarr[1, 1].plot(stairTime, par1stairsY, color='g')
axarr[1, 1].plot(stairTime, par1stairsZ, color='r')
axarr[1, 1].set_title('Going Up\Down Stairs')
axarr[1, 1].set_xlabel('time(s)')
axarr[1, 1].set_ylabel('normalized magnitude')
plt.tight_layout() # fix layout overlap
plt.show()

