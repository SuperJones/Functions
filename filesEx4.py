import turtle

labfile = open("C:\Users\NinjaZeroOne\Desktop\httlacs\labdata.txt", 'r')


def average(yourList):
    theSum = 0 
    for i in yourList:
    	i = int(i)
        theSum = theSum + i
	finalNum = theSum / (len(yourList) -1)
    return finalNum

def sumthem(yourFile, x_or_y):
    newline = yourFile.readline()
    add_them = 0
    while newline:
        values = newline.split()
        add_them = add_them + (int(values[x_or_y]))
        newline = yourFile.readline()
    return add_them

def m_formula(numPoints)
	m = (the sum of x times the sum of y) - ( n times mean of x values times mean of y values)
	and (sum of x values square)- (n times (the mean of x values squared))
	return 0

def plotRegression(line):
	reads the data from the file and uses a turtle to plot points

#n equals the number of points which is the number of lines in the file 
linelist = f.readlines()
n = (len(linelist) + 1)

x_sum = sumthem(labfile, 0)
y_sum = sumthem(labfile, 1)

y = (the sum of y values) + (m_formula(n)) times (x - (sum of x values))





xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()
wn.setworldcoordinates(0-border, 0-border, 40*numbars+10, maxheight+10)
#Make the window fit the data

while line:
    values = line.split()
    print (values[0], "average is", average(values[1:]))
    line = infile.readline()

f.close()
wn.exitonclick