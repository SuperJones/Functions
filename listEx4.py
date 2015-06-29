import random

beginList = []
for i in range(10):
	addNum = random.randrange(0, 1000)
	beginList.append(addNum)
	
print(typebeginList)

	
#Write a function called average that will take the list as a parameter
#and return the average.
	
def average(yourList):
    theSum = 0 
    for i in yourList:
        theSum = theSum + i
    return theSum
		
print(average(beginList))
