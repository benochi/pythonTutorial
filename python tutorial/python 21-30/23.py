#x = lambda a, b, c : a + b + c
#print(x(5, 5, 2))

def myfunc(n):
  print(n)
  return lambda a: a * n

double = myfunc(2)
triple = myfunc(3)

print(double(10))
print(triple(10))