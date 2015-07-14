#Write a recursive function to reverse a list

def lsReverse(numlist, new_list = []):
    if len(numlist) == 0:
        return new_list
    else:
    	new_list.append(numlist[-1])
    	numlist.pop(-1)
    	return lsReverse(numlist)

print(lsReverse([1,3,5,7,9]))
print(lsReverse([74, 2, 5, 32, 100]))