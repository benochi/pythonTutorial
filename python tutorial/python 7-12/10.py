

#print(x[-2:-1])
"""
if "five" in x:
  print("I found one!")
else: 
  print("I did not find five.")

"""
"""
x = ["one", "two", "three", "four"]
y = ("tuple1", "tuple2")

x.extend(y)

print(x)
"""
"""
x = ["one", "two", "three", "four"]

x.clear()

print(x)
"""
"""
x = ["one", "two", "three", "four", "five", "six"]


for i in range(len(x)):
  print(x[i])
"""
"""
x = ["one", "two", "three", "four", "five", "six"]

i = 0
while i < len(x):
  print(x[i])
  i = i + 1
"""
x = ["one", "two", "three", "four", "five", "six"]
[print(num) for num in x] #list comprehension 