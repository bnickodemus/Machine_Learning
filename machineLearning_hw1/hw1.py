import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
        
# graph 1 (race compared to salary)
race = np.genfromtxt('adult.data', delimiter=',', dtype=None, usecols=(8))
salary = np.genfromtxt('adult.data', delimiter=',', dtype=None, usecols=(14))

for r in np.unique(salary):
    i = np.char.equal(salary,r) # i is a list of of true and false

raceArray = []
perc = []

for r in np.unique(race):
    raceArray = np.char.equal(race,r) 
    ws = salary[raceArray] # these are salaries of races
    i = np.char.equal(ws,' >50K')
    c = Counter(i) # dictionary on keys counting 
    #print c 
    total = float(c[1]) / float(c[0] + c[1]) # amount true/total
    perc.append(total)

plt.bar(np.arange(len(perc)),perc)
plt.xlabel('Race')
plt.ylabel('Percent earning more than 50K')
plt.title('Average salary earned by race')
labels = ['Indian','Asian','Black','Other','White']
plt.xticks(np.arange(len(perc)),labels)
plt.show()

# graph 2 (age compared to salary)
age = np.genfromtxt('adult.data', delimiter=',', dtype=None, usecols=(0))
age = np.char.mod('%d', age)
for r in np.unique(salary):
    i = np.char.equal(salary,r) # i is a list of of true and false
    
ageArray = []
salaryPercent = []
ages = []

for r in np.unique(age): # for each unique age
    ageArray = np.char.equal(age,r)
    ws = salary[ageArray] # salaries by age
    i = np.char.equal(ws, ' >50K')
    c = Counter(i)
    #print c
    if len(c) == 2: # if length == 1 then there were no true values
        total = float(c[1]) / float(len(age)) 
        salaryPercent.append(total) # total is the trueValues/totalNumber
        ages.append(int(r))
        #print total

plt.bar(ages,salaryPercent)
plt.xlabel('Age')
plt.ylabel('Percent earning more than 50K')
plt.title('Average salary earned per age')
plt.show()

# graph 3 (education compared to working overtime)
education = np.genfromtxt('adult.data', delimiter=',', dtype=None, usecols=(3))
hoursPerWeek = np.genfromtxt('adult.data', delimiter=',', dtype=None, usecols=(12))
        
educationArray = []
hoursPercent = []

for r in np.unique(education): # for each unique education
    educationArray = np.char.equal(education,r)
    ws = hoursPerWeek[educationArray]
    data = np.array(ws)
    i = data > 40 # i is a boolean vector
    c = Counter(i)
    hoursPercent.append(float(i[1]))
 
plt.plot(range(16), hoursPercent, '*')
plt.title('Education associated with working overtime')
plt.xlabel('Education')
plt.ylabel('overtime hours worked (40+)')
labels = ['10th','\n11th','12th','\n1-4','5-6','\n7-8','9th','\nacdm','voc','\nbach','doc','\nhs-grad','masters','\npre','prof','\nsome\ncollege']
plt.xticks((range(16)),labels)
labels2 = ['straight-time','overtime']
plt.yticks((range(2)),labels2)
plt.show()
