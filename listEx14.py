def replace(s, old, new):
    tempString = s.split(old)
    return tempString       

stringMaybe = 'I love spom!  Spom, yum!'
print(replace(stringMaybe, 'om', 'am'))

