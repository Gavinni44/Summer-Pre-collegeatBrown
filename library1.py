from math import pow
from math import sqrt
from random import randint
from random import shuffle
from random import choice


x = pow(5,4)
print("result 1 is", x)

y = sqrt(16)
print("y is", y)

a = randint(0,100)
print("a is", a)

names = ["Max", "Matthew", "Attila", "Tobal", "Brayson", "Evan"]
print("Original names: ", names)

shuffle(names)
print("Names after shuffling: ",names)

chosen = choice(names)
print("Chosen name is: ",chosen)