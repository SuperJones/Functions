infile = open("C:\Users\NinjaZeroOne\Desktop\studentdata.txt", 'r')
line = infile.readline()

while line:
    values = line.split()
    if len(values) > 7:
        print(values[0])
    line = infile.readline()

infile.close()