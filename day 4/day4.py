contained =0
import numpy as np
with open("input.txt") as f:
    for line in f:
       array1 = np.zeros[99] #make an array of 99 zeros
       array2 = np.zeros[99]  
       schedule = line.split(",")
       sched1index = schedule[0].split("-")
       sched2index = schedule[1].split("-")
       for i in range(sched1index[0],sched1index[1]):
        array1[i] = 1
       for j in range(sched2index[0],sched2index[1]):
        array2[j] = 1
       mask = array1 | array2
       if mask == array1:
        contained += 1
       elif mask == array2:
        contained += 1
    print(contained)