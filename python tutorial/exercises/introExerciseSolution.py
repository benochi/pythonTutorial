#import the module you made AND rename it
import storeItems as s
import re

#assign the data objects that you built (Set, List, Tuple, Dict) from your module
free = s.freeItems
cheap = s.cheapItems
moderate = s.moderateItems
expensive = s.expensiveItems

#print one of the unpacked variables from your module
print("I unpacked: " + s.x)

#add user input asking for a first and last name
fullName = input("What is your first and last name?")

#use the split method to cut the string into first and last name
firstName = fullName.split(" ")[0]
lastName = fullName.split(" ")[1]
#capitalize the first letter in each name 
firstCap = firstName.capitalize()
lastCap = lastName.capitalize()

#return a string and concatonate using the + operator to say "Your first name is <firstName> and your last name is <lastName>" 
#using the users inputed names in place of the placeholders in my example. 
print("Your first name is " + firstCap +" and your last name is " + lastCap)

#add user input in the CLI(command line interface) and assign it to a variable
itemToGet = input("Would you like a free, cheap, moderate, or expensive item? ")

#build a if/elif/else to handle user input and check the user input string equality with a comparison operator(==)
#if user input does NOT equal the options given, pass
if(itemToGet == 'free'):
  #print an item from the tuple by index
  print(free[0])
elif(itemToGet == 'cheap'):
  #print the set, remember how indexing and slicing don't work in sets like other objects. 
  print(cheap)
elif(itemToGet == 'moderate'):
  #print an item from the list by index
  print(moderate[2])
  #Extra credit - check the dict item to see if it returns a True or False boolean value and modify output accordingly. 
  #In the case of my example, it would be checking if the item is 'inStock' 
  #If you want practice you can play around with the 'and' operator, but for my example a nested if(): makes more sense. 
elif(itemToGet == 'expensive'):
  if(expensive[1]['inStock'] == True):
    #print an item from the dict by index and return the name value by using the key 'name'
    print(expensive[1]['name'])
  else:
    print("That item is sold out.")
else:
  pass

#make a list of imaginary clients and
customers = ['Ashley', 'Dan', 'Dustin', 'Aaron']

#build a method that loops over that list, printing each of them.
def print_customers(customers):
  for customer in customers:
    print("Customer " + customer + " entered the store.")

#execute that method Be sure to pass in any necessary arguments.
#The proper scope should have the list outside of the method. 
print_customers(customers)

#write a lambda method that multiplies an arg by .07%
taxable = lambda a: a * .07

#assign the price of an item in your dict to a variable
price = expensive[1]['price']

#use the lambda function to find the tax of the item price. 
tax = taxable(price)

#add the tax and the original price for the total price and print that total
#Extra credit - Use format to make sure only 2 decimals are returned
total = tax + price
txt = "Your total is {price:.2f}!"
print(txt.format(price = total))
#Note - think about using ceil / floor to round change if needed. Remember to import Math if you try this.

#build a while loop that pops customers from the list, prints the customer and stops when the list is empty. 
#be careful to make it stop if there are no customers and Ctrl+C is your friend. 
while(len(customers) > 0):
  leaving = customers.pop()
  print(leaving + " is leaving the store.")

#build a customer class
#give customers an __init__ a name and an age.
class Customer:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def greeting(self):
    print("Hello, my name is " + self.name)

#make a customer
c1 = Customer("Billy", 12)

#print the customers name and age
print(c1.name, c1.age)

#add a customer method to your class that says "My name is " and uses their name.
#do this in the base class and call that function here. 
c1.greeting()

#modify the customer age and print it
c1.age = 22
print(c1.age)

#now make a child class that inherits from the Customer class
#Remember you can pass to give it the same attributes only. 
class CustomerChild(Customer):
  pass

#use the child to create an object instance
c2 = CustomerChild("Tammy", 50)
#use the parents function on the child
c2.greeting()


#make an iterator for the tuple, in my example it is 'free'
#Lists, Tuples, dictionaries, and sets are all iterable in this fashion
myIt = iter(free)

#print a few values using the iterator and keyword next
print(next(myIt))
print(next(myIt))

#practice scope 
#Make a method that has a global variable inside of it and assigns a value to that variable
def scopeCheck():
  global imAGlobalVar
  imAGlobalVar = 100

#call the method
scopeCheck()

#print the global variable outside of the method
print(imAGlobalVar)

#import the regex module at the top it is called 're'
#make a variable with a string value

randomTxt = "This is a random text string."

#use regex to search for matching words in the string
regexSearch = re.search("^This.*string.$", randomTxt)
#print the results, if you are getting "None", check your work.
print(regexSearch)

#build a try/except/finally block and have it return an error
#this is the last thing our application does, so feel free to play around with it. 
giraffe = None
try:
  print(giraffe)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
