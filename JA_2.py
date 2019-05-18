import random

#create empty list
list = []

#populate with random number
for x in range(1000):
    list.append(random.randint(10,1000))

#set initial points of min and max
min = list[0]
min_ind =0
max = list[0]
max_ind =0
total = 0

#search min and max and calculate total
for ind, val  in enumerate(list):
    if(min>val):
        min=val
        min_ind= ind
    if(max<val):
        max=val
        max_ind=ind
    total +=val

#calculate mean
mean = total / 1000

#print min and max
print("minimum number ",min ," at ", min_ind)
print("maximum number ",max ," at ", max_ind)
print("mean ",mean)





