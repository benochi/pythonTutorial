#x = ("a","b")

"""
import timeit

x = timeit.timeit(stmt="[1,2,3,4,5]", number=10000000)
y = timeit.timeit(stmt="(1,2,3,4,5)", number=10000000)

print("List: ", x)
print("Tuple: ", y)
"""
"""
x = ("one",)
y = ("one", "two", "two")
print(x)
print(y)
"""
"""
x = ("one", 1, True)
print(x)
print(type(x))
"""
"""
x = tuple(("one", "two"))

print(x)
"""

x = ("One", "two", 3, 4)
#print(x[-2])
#print(x[0:3])
if "two" in x:
  print("Yes, two is in x.")

