from test import testEqual
def removeWhite(s):
    new_string = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for achar in s:
        if achar in alphabet:
            new_string = new_string + achar
    return new_string
 
 
def isPal(s):
    return False
 

userString = raw_input("Please enter Palindrome: ")
print(removeWhite(userString))

 
testEqual(isPal(removeWhite("x")),True)
testEqual(isPal(removeWhite("radar")),True)
testEqual(isPal(removeWhite("hello")),False)
testEqual(isPal(removeWhite("")),True)
testEqual(isPal(removeWhite("hannah")),True)
testEqual(isPal(removeWhite("madam i'm adam")),True)
 

 