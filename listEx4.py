import random

beginList = []
for i in range(100):
	addNum = random.randrange(0, 1000)
	beginList.append(addNum)
	
print(beginList)

	
#Write a function called average that will take the list as a parameter
#and return the average.
	
def average(yourList):
    theSum = 0 
    for i in yourList:
        theSum = theSum + i
		print(theSum)
	finalNum = theSum / (len(yourList))
    return finalNum
		
print(average(beginList))
