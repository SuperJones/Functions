myList = [76, 92.3, "hello", True]
myList.append(4)
print(myList)

myList = myList + [76]
print(myList)

#Append “apple” and 76 to the list.
myList.append("apple")
myList.append(76)
print(myList)

#Insert the value “cat” at position 3.
myList.insert(3, "cat")
print(myList)

#Insert the value 99 at the start of the list.
myList.insert(0, 99)
print(myList)

#Find the index of “hello”.
print(myList.index("hello"))

#Count the number of 76s in the list
print(myList.count(76))

#Remove the first occurrence of 76 from the list.
myList.remove(76)
print(myList)

#Remove True from the list using pop and index.
findBool = myList.index(True)
myList.pop(findBool)
print(myList)


