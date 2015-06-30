def oddNum(yourList):
    counter = 0
    for i in yourList:
        if len(i) == 5:
            counter = counter + 1
        else:
            counter = counter + 0
    return counter

print (oddNum (["Julie", "Sister", "Crazy", "pop", "stan", "crisp"]))

