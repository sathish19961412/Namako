# Create a Function:

def my_function():
    print("Welcome to sathish")


my_function()


# Calling a Function

def my_function1():
    print("Welocme come Back")


my_function1()


# Arguments in Function

def my_function2(name):
    print(name + "Class")


my_function2('First')
my_function2('Second')
my_function2('Thrid')


# Number Of Arguments

def my_function3(fname, lname):
    print(fname + "" + lname)


my_function3("sathish", "Mathew")
my_function3("Guru", "Prasath")


# my_function3("sathish", "Mathew")

def my_function4(*kids):
    print("Welcome to" + " " + kids[1])


my_function4("raj", "sathish", "Guru")


# Keyword Arguments

def my_function5(child3, child2, child1):
    print("How are you" + " " + child3)


my_function5(child1="sathish", child2="raj", child3="Mathew")


# Arbitrary Keyword Arguments, **kwargs
def my_function6(**kid):
    print("Wecome Back" + " " + kid["lname"])


my_function6(fname="Guru", lname="Prasath1")


# Default Parameter Value

def my_function7(country="Norway"):
    print("I am from " + country)


my_function7("Sweden")
my_function7("India")
my_function7()
my_function7("Brazil")


# Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)


fruits1 = ["apple", "banana", "cherry"]

my_function(fruits1)


# Return Values

def my_fun(x):
    return 5 * x


print(my_fun(4))
print(my_fun(7))
print(my_fun(5))


# The pass Statement

def fun1():
    pass
