#from test import testEqual

def removeWhite(s):
    new_string = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for achar in s:
    	achar = achar.lower()
        if achar in alphabet:
            new_string = new_string + achar
    return new_string
 
def reverse(newString):
    convertString = newString
    if len(convertString) == 1:
        return convertString[0]
    else:
        return reverse(convertString[1:]) + convertString[0]

def isPal(almostFinalString):
    ThisIsIt = reverse(almostFinalString)
    if ThisIsIt == almostFinalString:
        return True
    else:
        return False
 

userString = raw_input("Please enter Palindrome: ")
print(isPal(removeWhite(userString)))



#testEqual(isPal(removeWhite("x")),True)
#testEqual(isPal(removeWhite("radar")),True)
#testEqual(isPal(removeWhite("hello")),False)
#testEqual(isPal(removeWhite("")),True)
#testEqual(isPal(removeWhite("hannah")),True)
#testEqual(isPal(removeWhite("madam i'm adam")),True)
 

 