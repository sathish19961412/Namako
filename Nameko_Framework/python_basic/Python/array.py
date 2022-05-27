# Basic arrya
cars = ["BMW", "Ford", "Volvo"]
print(cars)
# Access the Elements of an Array

x = cars[2]
print(x)

# Modify the value of the first array item:
y = cars[0] = "Toyota"
print(y)

# The Length of an Array
z = len(cars)
print(z)

# arrys in loops

for a in cars:
    print(a)

# Adding Array Elements
cars.append("Honda")
print(cars)

# pop Array Elements
cars.pop(0)
print(cars)

# remove Array Elements
cars.remove("Ford")
print(cars)
