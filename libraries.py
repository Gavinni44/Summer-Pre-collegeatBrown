
import math
import random

x = math.pow(5,4)
print("x is", x)

y = math.sqrt(16)
print("y is", y)

a = random.randint(0,100)
print("a is", a)

names = ["Max", "Matthew", "Attila", "Tobal", "Brayson", "Evan"]
print("Original names: ", names)

random.shuffle(names)
print("Names after shuffling: ",names)

chosen = random.choice(names)
print("Chosen name is: ",chosen)