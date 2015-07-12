import string
 
infile = open("C:\Users\NinjaZeroOne\Desktop\httlacs\AliceInWonderland.txt", 'r')
 
aliceDiction = {}   #create empty dictionary
 
aliceDiction = {}           #create empty dictionary
 
for aline in infile:  
    for aword in aline.split():        
        
        # remove punctuation
        aword = aword.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        aword = aword.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        aword = aword.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        aword = aword.replace(']', '').replace(';', '')
        
        aword = aword.lower()

        if aword.isalpha():             #Make sure it is not a number
            if aword in aliceDiction:  #Check to see if word is in dictionary
                aliceDiction[aword] = aliceDiction[aword] + 1
            else:
                aliceDiction[aword] = 1
 
    
keys = aliceDiction.keys()
keys.sort()

ks = list(aliceDiction.keys())           
j = 0   
largest_word = 0        
for akey in ks:
    if len(akey) >= j:
        largest_word = akey
        j = len(akey)           
   
 
 
print(largest_word)
 
infile.close()
