score = 0
bonusdict = {'A':1, 'B':2, 'C':3,'X':1, 'Y':2, 'Z':3}
op = "A"
me = "X"
#X= lose
#Y= Draw
#Z= Win
with open("input.txt") as f:
    for line in f:
        op = line[0]
        me = line[2]
        if (me == 'Y'): #Covers all tying cases
            score += 3
            score += bonusdict[op]
        elif (me == 'X'): #lose all of these
            if (op == 'A'):
                score += bonusdict["C"]
            elif (op == 'B'):
                score += bonusdict['A']
            elif (op == 'C'):
                score += bonusdict['B']    
        elif (me == 'Z'): #Win all of these
            if (op == 'A'):
                score += bonusdict["B"]
            elif (op == 'B'):
                score += bonusdict['C']
            elif (op == 'C'):
                score += bonusdict['A']   
            score += 6 
print(score)          