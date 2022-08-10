#Make a tuple and add 3 items to it
freeItems = (
  'straw',
  'napkin', 
  'ketchup'
  )

# build a set and add at least 3 items to it
cheapItems = {
  'cookie',
  'soda',
  'water',
  'chips'
}

#build a list and add at least 3 items to it
moderateItems = [
  "energy drinks",
  "sandwhich",
  "beer"
]

# build a dict where the key is an int that corresponds to the index and the VALUE is a Dict containing the following data as key value pairs
# name(string), price(float), quantity(int), inStock(boolean)
expensiveItems = {
  0: {
    'name':'12 pack',
    'price':22.99,
    'quantity': 2,
    'inStock': True
  },
  1: {
    'name':'pizza',
    'price':10.99,
    'quantity': 4,
    'inStock': True
  }
}

#unpack the list into individual variables
x, y, z = moderateItems
