#Used answer to Exercise 11 as base and edited.

def sum(lst):
    index = 0
    while lst[index] != "sam" and index < len(lst):
        index = index + 1
    if lst[index] == "sam":
        index = index + 1
    return index

lst = ["aubrey", "tim", "laura", "lilly", "jo", "bob", "sam", "dave", "scott"]

print(sum(lst))

#Remember: When you need to do something at least one time and continue 
#to do it until a boolean is met, try a while loop. 