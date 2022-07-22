class Student : 
    def __init__(self, name, age, grade) :
        self.name = name
        self.age = age
        self.year = grade

    def myfunc(self) :
        print("Student's name is " + self.name)
        
        

x = Student("Josh", 15, "9th")
x.myfunc()
print(x.age)
print(x.year)

class Course :
    def __init__(self, name, room) :
        self.name = name
        self.room = room

    def myfunc(self) :
        print("Welcome to " + self.name)

p1 = Course("Physics", "Room 205")
p1.myfunc()
print(p1.room)