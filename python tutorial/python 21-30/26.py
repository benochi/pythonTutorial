
#parent / base class 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greeting(self):
    print("Hello, I am " + self.name)

p1 = Person("Bob", 21)

#p1.greeting()

#child class/derived class
class Kid(Person):
  def __init__(self, name, age, favColor):
    super().__init__(name, age)
    self.favColor = favColor

  def greeting(self):
    print("My favorite color is " + self.favColor)

k1 = Kid("Mini-Bob", 12, "red")
print(k1.age)
k1.greeting()
#k1.color()
#k1.favColor = "blue"
#print(k1.favColor)