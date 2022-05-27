# Python Classes and Objects
# Create Object

class Myclass1:
    x = 4


p1 = Myclass1()
print(p1.x)


# The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("sathish", 25)

print(p1.name)
print(p1.age)


# Object Methods

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfirst(self):
        print("How old are You Nithya", self.age)


p1 = Person1("Guru", 22)
p1.myfirst()
print(p1.age)
print(p1.name)

# Modify Object Properties
p1.age = 25
print(p1.age)


# pass
class Person2:
    pass


# Delete Object Properties
# Delete the age property from the p1 object:
p1 = Person1("Guru", 22)
del p1.age
print(p1.age)

# Delete the p1 object:
del p1
