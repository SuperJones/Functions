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


