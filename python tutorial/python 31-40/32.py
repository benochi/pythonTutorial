#JSON - Javascript object notation
import json

"""
x = '{"name":"bob", "age":30}'

y = json.loads(x)

print(y["age"])
"""
#python dict
x = {
  "name":"bob",
  "age":30,
  "color":"red"
}

# to JSON

y = json.dumps(x)

#print(y) 
a = {
  "list":["list1", "list2"],
  "tuple":("Tuple", "Tuple2"),
  "string":"I'm a string",
  "integer":42,
  "float":31.76,
  "Boolean":True,
  "Boolean":False,
  "stuff":None
}

print(json.dumps(a, indent=4, sort_keys=True))

#dict	Object
#list	Array
#tuple	Array
#str	String
#int	Number
#float	Number
#True	true
#False	false
#None	null

