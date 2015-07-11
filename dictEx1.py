#Write a program that allows the user to enter a string. 
#It then prints a table of the letters of the alphabet in 
#alphabetical order which occur in #the string together with the 
#number of times each letter occurs. Case should be ignored. 

import string
 
userString = (raw_input("Please enter a sentence: "))
 
userString = userString.lower()
 
stringDiction = {}
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