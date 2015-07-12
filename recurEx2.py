#Write a recursive function to reverse a list

def lsReverse(numList):
    new_list = []   
    if len(new_list) == len(numList):
        return new_list
    else:
        return numList[len(numlist) - 1] + lsReverse(numlist[0:(len(numlist) - 1)])

print(lsReverse([1,3,5,7,9]))