def replace(s, old, new):
    tempString = s.split(old)
    glue = new
    newString = glue.join(tempString)
    return newString

stringMaybe = 'I love spom!  Spom, yum!'
print(replace(stringMaybe, 'om', 'am'))