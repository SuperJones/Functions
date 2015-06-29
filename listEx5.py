import random

beginList = []
for i in range(10):
	addNum = random.randrange(0, 1000)
	beginList.append(addNum)
	
print(beginList)

	
#Write a function called average that will take the list as a parameter
#and return the average.
	
def max(yourList):
    max = 0 
    for i in yourList:
        if i > max:
	        max = i
    return max
		
print(max(beginList))


