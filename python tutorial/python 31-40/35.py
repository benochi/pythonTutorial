"""
try:
  print(x)
except NameError:
  print("x is not defined")
else: 
  print("It worked fine")
finally: 
  print("I am the finally block")
  """
"""
try:
  f = open("demo.txt")
  try:
    f.write("Hi")
  except:
    print("File is invalid")
  finally:
    f.close()
except:
  print("Something is broken!")
  """

x = 0
if x < 10:
  raise TypeError("Error message")