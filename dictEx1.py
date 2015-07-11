#Write a program that allows the user to enter a string. It then prints a #table of the letters of the alphabet in alphabetical order which occur in #the string together with the number of times each letter occurs. Case #should be ignored. A sample run of the program might look this this:


userString = (raw_input("Please enter a sentence: "))
 
for achar in userString:
    alpha_count = {}
    compare_alpha = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if achar in compare_alpha:
        if achar.isalpha:
        else:
    else: