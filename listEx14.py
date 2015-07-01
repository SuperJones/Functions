
def replace(s, old, new):
    newString = ''
    for i in s:
        if i == new:
            #change it
            old = new
            newString = newString + new
        else:    
            #leave it
            newString = newString + i
    return newString       

stringMaybe = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
print(replace(stringMaybe, 'om', 'am'))