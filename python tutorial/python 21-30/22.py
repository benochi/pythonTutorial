#def function1(name, lname):
#  print("I'm a function named " + name + lname)

#function1("Bob")
#function1("Sam.")
#function1("Miranda")
"""
def function2(item1, item2, item3):
  print("Grocery item: " + item3)

function2(item3 = "carrots", item1 ="milk",item2 ="tea")
"""
#kwargs
"""
def function3(**person):
  print("My last name is " + person["lastname"])

function3(firstname="bob", lastname="Rogers")
"""
"""
def function4(name = "Bob"):
  print("My name is " + name)

function4("Steve")
function4("Robert")
function4()
function4("Dave")
"""
"""
def function5(names):
  for name in names:
    print(name)

people = ["Bob", "Dave", "Robert"]

function5(people)
"""
"""
def function6(num):
  return 2 * num

def function7(num):
  x = function6(num)
  print(x)

function7(2)
function7(4)
function7(6)
"""
"""
def function8():
  pass

function8()
"""

## recursion 
def exFunc(k):
  if(k > 0):
    result = k + exFunc(k -1)
    print(result)
  else:
    result = 0
  return result


exFunc(6)