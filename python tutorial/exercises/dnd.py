#OOP
"""
4 pillars of OOP:
Inheritance: The ability of an object in a subclass to inherit the behaviors and attributes from its parent class.

Abstraction: A process where you show only “relevant” data and “hide” unnecessary details of an object from the user. 
-> User only needs to know how to interact with program. 

Polymorphism: The ability of a function or method to operate on many different types. For example, print(len("hello")
In OOP, this also allows us to define methods in a child class with the same name as one in the 
parent class (called Method Overriding).

Encapsulation: The ability to wrap data (variables) and methods in a single unit (such as a class) to restrict direct
 access to them and prevent accidental modification.
"""

import random

class CharacterDice:
  #take num as arg and return random value 0 - arg
  def roll(self, num = 0):
    return random.randint(0, num)

  # 0 20 + mod  
  def skillCheck(self, modifier =0):
    die = random.randint(0, 20)
    #print(modifier)
    return (die + modifier)

class PlayerCharacter(CharacterDice):
  def __init__(
    self,
    name=None,
    race=None,
    size=None,
    alignment=None,
    armorClass=None,
    hp=None,
    strength=None,
    constitution=None,
    dexterity=None,
    intelligence=None,
    wisdom=None,
    charisma=None
  ):
    self.name=name
    self.race=race
    self.size=size 
    self.alignment=alignment
    self.armorClass=armorClass 
    self.hp=hp
    self.strength=strength
    self.constitution=constitution
    self.dexterity=dexterity
    self.intelligence=intelligence
    self.wisdom=wisdom
    self.charisma=charisma

testguy = PlayerCharacter(
  name="TestGuy",
  race="hooman",
  size="medium",
  alignment="Chaotic-Neutral",
  armorClass=10,
  hp=12,
  strength=18,
  constitution=17,
  dexterity=11,
  intelligence=11,
  wisdom=7,
  charisma=4
)

#print(CharacterDice.roll(20))
#print(CharacterDice.skillCheck(7))

#print(testguy.name, testguy.strength)

print(testguy.roll(20))
print(testguy.skillCheck(7))