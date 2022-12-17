score = 0
def isoverlap(a1,a2,b1,b2):
    if a1<=b2 and a2>=b1:
        return True
    else:
        return False
with open("day 4\input.txt") as f:
    for line in f:
        schedule = line.split(",")
        range1 = schedule[0].split("-")
        range2 = schedule[1].split("-")
        if (isoverlap(int(range1[0]),int(range1[1]),int(range2[0]),int(range2[1]))):
            score += 1
        elif (isoverlap(int(range2[0]),int(range2[1]),int(range1[0]),int(range1[1]))):
            score += 1
    print(score)
            

