#Write a recursive function to compute the factorial of a number.

def factNum(userNum):
   if userNum <= 1:
        return userNum
   else:
        return userNum * factNum(userNum - 1)

print(factNum(4))