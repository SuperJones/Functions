#write a program that calculates the average grade for each student, 
#and print out the student’s name along with their average grade.


infile = open("C:\Users\NinjaZeroOne\Desktop\httlacs\studentdata.txt", "r")
line = infile.readline()

def average(yourList):
    theSum = 0 
    for i in yourList:
    	i = int(i)
        theSum = theSum + i
	finalNum = theSum / (len(yourList) -1)
    return finalNum


while line:
	#remember - the above while line means while the content of 
	#line is not the empty string.
	values = line.split()
	print (values[0], "average is", average(values[1:]))
    line = infile.readline()
    
infile.close()