#write a program that calculates the average grade for each student, 
#and print out the student’s name along with their average grade.


infile = open("C:\Users\NinjaZeroOne\Desktop\studentdata.txt", "r")
line = infile.readline()

def average(yourList):
	theSum = 0
	for i in yourList:
        theSum = theSum + i
	return theSum
	
#first I need the to separate the numbers and turn them into ints
def separate (your_file):
	values = your_file.split()
	finalNum = 0
	for anumber in values:
	    if anumber != values[0] and anumber < len(values):
	    	anumber = int(anumber)
	    	finalNum = finalNum + anumber
	    else:
	    	finalNum = finalNum + 0 
	return finalNum

print(separate(line))
#then I need to be able to add them and divide by the number of items
#then I need to be able to print the a returned value next to the name

    
infile.close()