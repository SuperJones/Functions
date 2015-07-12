pirate_dict = {'man': 'matey', 'is':'b', 'hello':'avast', 
               'my':'me', 'restroom':'head', 'the':"th'", 
              'lawyer':'foul blaggart', 'are':'be', 
               'students':'swabbies', 'excuse':'arr' 'your':'yer',
               'restaurant':'galley', 'professor':'foul blaggart', 
               'madam':'proud beauty', 'boy':'matey', 'student':'swabbie',
               'hotel':'fleabag inn', 'sir':'matey'}

#Or I could create a file and create the dictionary based
#off the file.

ks = list(pirate_dict.keys())
j = 0
largest_word = 0
for akey in ks:
    if len(akey) >= j:
        largest_word = akey
        j = len(akey)            

print(largest_word)
