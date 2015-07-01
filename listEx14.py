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
print(replace(stringMaybe, 'om', 'am'))

#went back through reading and rediscovered the split and join method.
#so I have to figure out how to split it so that "om" comes out.
# and then join it with "am" in its place.