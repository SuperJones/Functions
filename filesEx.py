fileref = open('C:\Users\NinjaZeroOne\Desktop\httlacs\qbdata.txt', 'r')

for aline in fileref:
	values = aline.split()
	print('QB', values[0], values[1], 'had a rating of', values[10])

fileref.close()