pirate_dict = {'man': 'matey', 'is':'b', 'hello':'avast', 
               'my':'me', 'restroom':'head', 'the':"th'", 
              'lawyer':'foul blaggart', 'are':'be', 
               'students':'swabbies', 'excuse':'arr', 'your':'yer',
               'restaurant':'galley', 'professor':'foul blaggart', 
               'madam':'proud beauty', 'boy':'matey', 'student':'swabbie',
               'hotel':'fleabag inn', 'sir':'matey'}

#Or I could create a file and create the dictionary based
#off the file.

user_string = raw_input("Type in regular english sentence: ")
 
new_string = ""
for aword in user_string.split():
    if aword in pirate_dict.keys():
        new_string = new_string + pirate_dict.get(aword)
            
                  
 
print(new_string)
