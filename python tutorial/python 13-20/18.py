
"""
print(x.keys())

x["new key"] = "added"
print(x.keys())
"""
"""
print(x.values())

x["key"] = "changed!"

print(x.values())
"""
x = {
  "key": "value",
  "key2": "value2",
  "int": 1,
  "bool": True,
  "float": 2.2,
  "list": [1,2,3]
}
"""
print(x.items())

x["float"] = 4.4

print(x.items())
"""

if "key" in x:
  print("I found key in x!")