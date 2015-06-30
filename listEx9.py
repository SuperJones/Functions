def oddNum(yourList):
    counter = 0
    for i in yourList:
        if i % 2 == 0:
            counter = counter + 0
        else:
            counter = counter + i
    return counter

print (oddNum ([1,2,3,4,5,6,7,8,9,10,11]))

