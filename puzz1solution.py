sum = 0
list = []
with open("input.txt") as f:
    for line in f:
        try:
            num = int(line)
            sum += num
        except ValueError:
            list.append(sum)
            sum = 0

highest = 0
print(list)
for i in range(len(list)):
    if list[i] > highest:
        highest = list[i]
print(highest)

    
        
