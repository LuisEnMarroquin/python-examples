# From this video: https://www.youtube.com/watch?v=N4mEzFDjqtA&t=438s

import random
import sys
import os

# Single and double quotes are the same
print('Hello "World"')
print("Hello \"World\"")

# Variable
NAME = "Derek"
print(NAME)

MULTILINESTRING = '''
Datatypes: 5
- Numbers
- Strings
- Lists (in JS Arrays)
- Tuples (inmutable arrays)
- Dictionaries (Maps) (in JS: objects)
Algoritmic operators: 7
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus (division remainder)
** Exponent (exponential or power)
// Floor division (the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero)
'''

print(MULTILINESTRING)

# By convention multiword variables are named with underscores
QUOTE = "Always remember you are"
MULTI_LINE_QUOTE = ''' unique
just like everyone else'''
print(QUOTE + MULTI_LINE_QUOTE)
print("%s %s %s" % ('I like the quite', QUOTE, MULTI_LINE_QUOTE)) # Format print

# Print within the same line
print("I don't like ", end='')
print("newlines")

# Print white space in console
print('\n' * 5)

# Datatype: list
GROCERY_LIST = [
  'Juice', 'Tomatoes', 'Potatoes', 'Bananas'
]

print('First Item:', GROCERY_LIST[0])
GROCERY_LIST[0] = 'Green Juice'
print('First Item:', GROCERY_LIST[0])

# Print subset of a list
print(GROCERY_LIST[1:3])

# Combine lists
other_events = ['Wash Car', 'Pick Up Kids']
to_do_list = [other_events, GROCERY_LIST ]
print(to_do_list)

# Get second item of the second list
print(to_do_list[1][1])

# Add to array
GROCERY_LIST.append('Onions')
print(GROCERY_LIST)

# Add on specific index (position, itemToAdd)
GROCERY_LIST.insert(1, 'Pickle')
# Remove element
GROCERY_LIST.remove("Pickle")
# Sort array
GROCERY_LIST.sort()
# Reverse array
GROCERY_LIST.reverse()
# Remove array index
del GROCERY_LIST[4]
# Get list length
print(len(GROCERY_LIST)) # Also works with tuples
# Get list max
print(max(GROCERY_LIST)) # Also works with tuples
# Get list min
print(min(GROCERY_LIST)) # Also works with tuples

# Create tuple (list that can't change)
PI_TUPLE = (3,2,1,0)

# To change a tuple you can turn it to a list
NEW_TUPLE = list(PI_TUPLE)
# And then turn it again into a tuple
NEW_LIST = tuple(NEW_TUPLE)

# Dictionary (the same thing as a JS object)
SUPER_VILLAINS = {
  'Fiddler' : 'Isaac Bowin',
  'Captain Cold' : 'Leonard Snart',
  'Weather Wizard' : 'Mark Mardon'
}
print(SUPER_VILLAINS['Captain Cold'])
print(SUPER_VILLAINS.get('Captain Cold'))
print(SUPER_VILLAINS.keys())
print(SUPER_VILLAINS.values())

# Conditionals

age = 18
if age >= 21 :
  print('You can drive a tractor')
elif age >= 16 :
  print('You can drive a car')
else : print("You can't drive")

'''
&& === and
!= === not
|| === or
'''

if ((age >= 1) and (age <= 18)): # Double conditionals
  print('You get a taco')

# For loop

for x in range(0, 10):
  print(x, ' ', end='')

print('\n')

tacos_list = [
  'Al Pastor', 'Bistec', 'Frijoles'
]

for y in tacos_list:
  print(y)

for x in [1,2,3,4,5]:
  print(x)

NUM_LIST = [ [1, 2, 3], [10, 20, 30], [100, 200, 300] ]

for x in range(0,3):
  for y in range(0,3):
    print(NUM_LIST[x][y])

# While loop

RANDOM_NUM = random.randrange(0, 10)

while(RANDOM_NUM != 5):
  print(RANDOM_NUM)
  RANDOM_NUM = random.randrange(0, 10)

i = 0

while i<=20:
  if(i%2 == 0):
    print(i, end='')
  elif(i == 9):
    break # Exit loop
  else :
    i += 1
    continue # Skip the next instructions of the loop
  i += 1 # Will be skiped if there is a continue before

# Functions

def addNumber (fNum, lNum):
  sumNum = fNum + lNum
  return sumNum

print('\n', addNumber(1,4))

# User input

print('What is your name')
name = sys.stdin.readline()
print('Hello', name)

# Trim string
long_string = "I'll try that"
print(long_string[0:4]) # First 4 chars
print(long_string[-4]) # Last 4 chars

# Formatting
print('%c is my %s letter and my number %d number is %.5f' % ('x', 'favorite', 1, .14))

# Write file
test_file = open('test.txt', 'wb')
print(test_file.mode)
print(test_file.name)
test_file.write(bytes('Write me to the file\n', 'UTF-8'))
test_file.close() # Close file connection

# Open file
test_file = open('test.txt', 'r+') # r+ == reading and writing
text_in_file = test_file.read()
test_file.close()
print(text_in_file)

# Delete file
os.remove('test.txt')

# Object oriented programming
class Animal:
  # Properties
  __name = '' # If preceded with __ means that will be private
  __height = 0
  __weight = 0
  # Constructor
  def __init__(self, name, height, weight):
    self.__name = name # 'self' is the same as 'this' in JS
    self.__height = height
    self.__weight = weight
  # Methods
  def set_name(self, name): # Setter
    self.__name = name
  def get_name(self): # Getter
    return self.__name
  def toString(self):
    return "{} is {} cm tall and {} kilograms".format(self.__name, self.__height, self.__weight)
cat = Animal('Whiskers', 33, 10)
print(cat.toString())

# Inherit from class
class Dog(Animal):
  __owner = ''
  # Constructor
  def __init__(self, name, height, weight, owner):
    self.__owner = owner
    super(Dog, self).__init__(name, height, weight)
  # Methods
  def set_owner(self, owner): # Setter
    self.__owner = owner
  def get_owner(self): # Getter
    return self.__owner
  def toString(self):
    return "{} is {} cm tall and {} kilograms and his owner is {}".format(self.__name, self.__height, self.__weight, self.__owner)
