

#for i in x:
#  print(i)

#print("two" in x)

#for i in x:
#  print(i in x)



#print(x)

#x.add("four")

"""
x = {"one", "two", "three"}
y = [1,2,3]

x.update(y)
print(x)
"""
"""
x = {"one", "two", "three"}
#x.remove("two")
#x.discard("two")
y = x.pop()

print(y)
print(x)
"""
"""
x = {"one", "two", "three"}
#x.clear()
del x
print(x)
"""
"""
x = {"one", "two", "three"}

for i in x:
  print(i)
"""
#x = {"one", "two", "three", 4}
#y = {1,2,"three", 4}
"""
#z = x.union(y)
#x.update(y)
#print(y)

#x.intersection_update(y)
z = x.intersection(y)
print(z)
"""
"""
x = {"one", "two", "three", 4}
y = {1,2,"three", 4}

#x.symmetric_difference_update(y)
z = x.symmetric_difference(y)
#print(x.union(y))
print(z)
"""

#add()	Adds an element to the set

#clear()	Removes all the elements from the set

#copy()	Returns a copy of the set

#difference()	Returns a set containing the difference between two or more sets

#difference_update()	Removes the items in this set that are also included in another, specified set

#discard()	Remove the specified item

#intersection()	Returns a set, that is the intersection of two other sets

#intersection_update()	Removes the items in this set that are not present in other, specified set(s)

#isdisjoint()	Returns whether two sets have a intersection or not

#issubset()	Returns whether another set contains this set or not

#issuperset()	Returns whether this set contains another set or not

#pop()	Removes an element from the set

#remove()	Removes the specified element

#symmetric_difference()	Returns a set with the symmetric differences of two sets

#symmetric_difference_update()	inserts the symmetric differences from this set and another

#union()	Return a set containing the union of sets

#update()	Update the set with the union of this set and others