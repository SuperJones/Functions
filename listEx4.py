#Create a list containing 100 random integers between 0 and 1000.
#(use iteration, append, and the random module). 


import random

beginList = []
for i in range(10):
	addNum = random.randrange(0, 1000)
	beginList = beginList + [addNum]

print(beginList)

	



#Write a function called average that will take the list as a parameter
#and return the average.

