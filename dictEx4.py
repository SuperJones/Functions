import string
 
infile = open("", 'r')
outfile = open("alice_words.txt", 'w')
 
aliceDiction = {}           #create empty dictionary
 
for aline in infile:
    values = aline.split()  #split each line into words
    j = 0
    for aword in values:
        if len(aword) >= j:
            new_word = aword
            j = len(aword)           
        else:
            #what does it need to do if it is not greater than
 
   
 
 
print(aliceDiction[alice])
 
infile.close()
outfile.close()