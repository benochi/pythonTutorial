"""
x = ["one","two","three"]
y = list(x)
x.append("four")
print(x)
print(y)
"""
"""
x =["one", "two", "three"]
y = [1,2,3]

z = y + x
#print(z)

#for el in y:
#  x.append(el)

#print(x)

y.extend(x)
print(y)
"""
x = ["one","two", "three","Four"]

x.append("five")	#Adds an element at the end of the list

x.clear()	#Removes all the elements from the list

y = x.copy() #Returns a copy of the list

x.count("two")	#Returns the number of elements with the specified value

z = x.extend([1,2,3])	#Add the elements of a list (or any iterable), to the end of the current list

x.index("two")	#Returns the index of the first element with the specified value

x.insert(3, 'INSERT!')	#Adds an element at the specified position

x.pop()	#Removes the element at the specified position

x.remove("two")	#Removes the item with the specified value

x.reverse()	#Reverses the order of the list

x.sort()	#Sorts the list
