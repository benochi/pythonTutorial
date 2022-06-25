

#x["string"] = "Hello World"

#x.update({"bool": True})

#x.pop("string")
#x.popitem()
#del x["key2"]

#x.clear()

x = {
  "key": "value",
  "key2": "value",
  "string": "random string",
  "list": [1,2,3,4]
}

#for k, v in x.items():
#  print(k, v)


#y = dict(x)

"""
nested1 = {
  "key": "Value",
  "list": [1,2,3]
}

nested2 = {
  "key2": "Value2",
  "list2": [1,2,3]
}

nest = {
  "nested1" : nested1,
  "nested2" : nested2
}

print(nest)
"""

#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary