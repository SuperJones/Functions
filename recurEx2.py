#Write a recursive function to reverse a list

def lsReverse(numlist, new_list = []):
 
    if len(new_list) == len(numlist):
        return new_list
    else:
    	new_list.append(numlist[-1])
    	numlist.pop(-1)
    	return lsReverse(numlist)

print(lsReverse([1,3,5,7,9]))