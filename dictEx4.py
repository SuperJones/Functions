import string
 
infile = open("C:\Users\NinjaZeroOne\Desktop\httlacs\AliceInWonderland.txt", 'r')
 
aliceDiction = {}   #create empty dictionary
 
for aline in infile:
    values = aline.split()  #split each line into words
    for aword in values:    #check to see if word is in dictionary
        if aword in aliceDiction:
            aliceDiction[aword] = aliceDiction[aword] + 1
        else:
            aliceDiction[aword] = 1
           
j = 0           
for akey in aliceDiction.keys:
    if len(akey) >= j:
        largest_word = akey
        j = len(akey)           
 
   
 
 
print(aliceDiction[alice])
 
infile.close()
