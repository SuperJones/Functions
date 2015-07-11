import string
 
infile = open("C:\Users\ZeroNinjaOne\Desktop\httlacs\AliceInWonderland.txt", 'r')
outfile = open("alice_words.txt", 'w')
 
aliceDiction = {}           #create empty dictionary
 
for aline in infile:
    values = aline.split()  #split each line into words
    for aword in values:    #check to see if word is in dictionary
        if aword in aliceDiction:
            aliceDiction[aword] = aliceDiction[aword] + 1
        else:
            aliceDiction[aword] = 1
 
   
keys = aliceDiction.keys()
keys.sort()
 
 
 
infile.close()
outfile.close()