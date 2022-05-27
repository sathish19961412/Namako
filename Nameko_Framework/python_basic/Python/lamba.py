# Lambda Function
def myfunction(n):
    return lambda a: a * n


mydouble1 = myfunction(2)
print(mydouble1(22))


# Double Lambda Function
def fun2(n):
    return lambda a: a * n

mydouble2 = fun2(2)
mytriple2 = fun2(4)
print(mydouble2(11))
print(mytriple2(11))
