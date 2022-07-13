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


charList = ['name','race','size','alignment','AC','HP','Strength','Constitution','Dexterity','Intelligence','Wisdom','Charisma']
charBuild =[]

for s in charList:
  x = input("Enter Character " + s + ": ")
  charBuild.append(x)

charObj2 = PlayerCharacter(
  name = charBuild[0],
  race = charBuild[1],
  size= charBuild[2],
  alignment= charBuild[3],
  armorClass= charBuild[4],
  hp= charBuild[5],
  strength= charBuild[6],
  constitution= charBuild[7],
  dexterity= charBuild[8],
  intelligence= charBuild[9],
  wisdom= charBuild[10],
  charisma= charBuild[11]
)

print("Player character " + charObj2.name + " created successfully.")

"""
charName = input("Character name: ")
charRace = input("Character race: ")
charSize = input("Character size: ")
charAlign = input("Character alignment: ")
charAc = input("Character AC: ")
charHp = input("Character HP: ")
charStr = input("Character Strength: ")
charCon = input("Character Constitution: ")
charDex = input("Character Dexterity: ")
charInt = input("Character Intelligence: ")
charWis = input("Character Wisdom: ")
charCha = input("Character Charisma: ")
"""
"""
charObj = PlayerCharacter(
  name = charName,
  race = charRace,
  size= charSize,
  alignment= charAlign,
  armorClass= charAc,
  hp= charHp,
  strength= charStr,
  constitution= charCon,
  dexterity= charDex,
  intelligence= charInt,
  wisdom= charWis,
  charisma= charCha
)

print("Player character " + charObj.name + " created successfully.")

print(charObj.roll(20))
print(charObj.skillCheck(7))
"""

"""
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
"""

#print(CharacterDice.roll(20))
#print(CharacterDice.skillCheck(7))

#print(testguy.name, testguy.strength)

#print(testguy.roll(20))
#print(testguy.skillCheck(7))