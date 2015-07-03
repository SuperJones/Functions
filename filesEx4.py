f = open("C:\Users\NinjaZeroOne\Desktop\httlacslabdata.txt", 'r')
line = f.readline()


def average(yourList):
    theSum = 0 
    for i in yourList:
    	i = int(i)
        theSum = theSum + i
	finalNum = theSum / (len(yourList) -1)
    return finalNum


def m_formula(numPoints)
	m = (the sum of x times the sum of y) - ( n times mean of x values times mean of y values)
	and (sum of x values square)- (n times (the mean of x values squared))
	return 0

def plotRegression(line):
	reads the data from the file and uses a turtle to plot points


n = the number of points which is the number of lines in the file 

y = (the sum of y values) + (m_formula(n)) times (x - (sum of x values))


while line:
    values = line.split()
    print (values[0], "average is", average(values[1:]))
    line = infile.readline()