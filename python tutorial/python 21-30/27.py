#iter()
"""
sampleList = "string example"

for char in sampleList:
  print(char)
"""

class NumIterator:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

numclass = NumIterator()
myIter = iter(numclass)

for x in myIter:
  print(x)