from math import pow as who
from math import sqrt as what 

from random import randint as b1
from random import shuffle as b2
from random import choice as b3

x = who(5,4)
print("x is", x)

y = what(16)
print("y is", y)

a = b1(0,100)
print("a is", a)

names = ["Max", "Matthew", "Attila", "Tobal", "Brayson", "Evan"]
print("Original names: ", names)

b2(names)
print("Names after shuffling: ",names)

chosen = b3(names)
print("Chosen name is: ",chosen)