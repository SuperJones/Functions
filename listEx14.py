def replace(s, old, new):
    newString = ''
    for i in s:
        if i == old:
            #change it
            newString = newString + new
        else:    
            #leave it
            newString = newString + i
    return newString       

stringMaybe = 'I love spom!  Spom, yum!'
print(replace(stringMaybe, 'o', 'a'))