import math as w1

import random as w2

x = w1.pow(5,4)
print("result 1 is", x)

y = w1.sqrt(16)
print("y is", y)

a = w2.randint(0,100)
print("a is", a)

names = ["Max", "Matthew", "Attila", "Tobal", "Brayson", "Evan"]
print("Original names: ", names)

w2.shuffle(names)
print("Names after shuffling: ",names)

chosen = w2.choice(names)
print("Chosen name is: ",chosen)