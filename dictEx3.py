import string
 
infile = open("C:\Users\NinjaZeroOne\Desktop\httlacs\AliceInWonderland.txt", 'r')
#outfile = open("alice_words.txt", 'w')
 
aliceDiction = {}           #create empty dictionary
 
for aline in infile:
    values = aline.split()  #split each line into words
    for aword in values:    #check to see if word is in dictionary
       
        if aword in aliceDiction:
            aliceDiction[aword] = aliceDiction[aword] + 1
        else:
            aliceDiction[aword] = 1
 
  
print(aliceDiction)   
#keys = aliceDiction.keys()
#keys.sort()

#for aword in keys:
	#print(str(aword) + "" + str(aliceDiction[aword]))
    #outfile.write(aword + "" + str(aliceDiction[aword]) )
    #outfile.write('\n')

print("The word 'alice' appears " + str(aliceDiction['alice']) + "times in the book.")    
#outfile.close()