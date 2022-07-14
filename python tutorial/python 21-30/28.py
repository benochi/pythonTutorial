"""
x = 10

def myfunc():
  def innerfunc():
    x=90
    print(x)
    
  innerfunc()
  
print(x)

myfunc()
"""
x = 10

def myfunc():
  global x
  x = 100

print(x)
myfunc()

print(x)
