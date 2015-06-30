#Sum all the elements in a list up to 
#but not including the first even number.

def oddNum(yourList):
    counter = 0
    for i in yourList:
        if i % 2 == 1:
            counter = counter + i 
        else:
            counter = counter + 0
    return counter

print (oddNum ([1,55,37,9,7,101,100,79,88]))

