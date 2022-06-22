"""
x = ("one", "two", "three")
y = list(x)
y[1] = "inserted"
x = tuple(y)

print(x)
"""
"""
x = ("one", "two", "three")
y = list(x)
y.append("four")
x = tuple(y)

print(x)

"""
"""
x = ("one", "two", "three")
y =("four",)
x += y
print(x)
"""
"""
x = ("one", "two", "three")
del x

print(x)
"""

x = ("one", "two", "three", "four", "five")
(ten, *eleven, twelve, thirteen) = x


print(ten)
print(eleven)
print(twelve)
print(thirteen)