"""
class newClass:
  x = 5

one = newClass()

print(one.x)
"""
#__init__()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greeting(self):
    print("hello, I'm " + self.name)

p1 = Person("Bob", 21)


#print(p1.age)
#print(p1.name)
#p1.greeting()

#p1.age = 500
#del p1
print(p1.age)

class fake:
  pass

