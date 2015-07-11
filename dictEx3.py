import string
 
infile = open("C:\Users\ZeroNinjaOne\Desktop\httlacs\AliceInWonderland.txt", 'r')
outfile = open("alice_words.txt", 'w')
 
aliceDiction = {}           #create empty dictionary
 
for aline in infile:
    values = aline.split()  #split each line into words
    for aword in values:    #check to see if word is in dictionary
        if aword in
 
for achar in userString:
    if achar in string.ascii_lowercase:
        if achar in stringDiction:
            stringDiction[achar] = stringDiction[achar] + 1
        else:   
            stringDiction[achar] = 1
 
   
keys = stringDiction.keys()
keys.sort()
for achar in keys:
    print(achar, stringDiction[achar])
 
 
infile.close()
outfile.close()