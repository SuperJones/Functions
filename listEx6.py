def sum_of_squares(xs):
    theSquare = []
    for j in xs:
        new_list = j ** 2
        theSquare.append(new_list)
    finalNum = 0
    for i in theSquare:
	    finalNum = finalNum + i 
    return finalNum

print(sum_of_squares([2,3,4]))

#Write a function sum_of_squares(xs) that computes the sum of 
#the squares of the numbers in the list xs. 
#For example, sum_of_squares([2, 3, 4]) 
#should return 4+9+16 which is 29.
