#x = [1,2,3,4,5]
#y = []

#for num in x:
#  y.append(num)

# y = [num for num in x]
#y = [num for num in x if 1 in x]
"""
x = ["one", "two", "three"]
y =[num for num in x if num != "two"]

z = [num for num in range(10) if num <= 3]

print(y)
print(x)
print(z)
"""
"""
y = [1,2,3,4]
x = ['hello world' for x in y]

print(x)
print(y)
"""
"""
colors = ["red", "blue", "yellow", "green", "orange", "blue", "red"]

y = [x if x != "blue" else "black" for x in colors]

print(y)
"""

#companies = ["Word", "Alphabet", "Google", "Microsoft", "Amazon", "Dell"]
#companies.sort()

#print(companies)

x = [1,200, 8000, 4, 17, 28, 300]
#x.sort()
#x.sort(reverse = True)
#print(x)
"""
def myfunc(n):
  return abs(n - 175)

x.sort(key = myfunc)
print(x)
"""
"""
companies = ["Word", "Alphabet", "Google", "Microsoft", "Amazon", "Dell", 
              "word", "alphabet", "google", "microsoft", "amazon", "dell"
            ]

companies.sort(key = str.lower)
print(companies)
"""

x = [1,2,3,4,5]
x.reverse()
print(x)