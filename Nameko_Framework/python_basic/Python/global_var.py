#create gloable Variable
from re import X


d=14
O=12
b=1996
def sathish():
    print("sathish D:O:B",d,O,b)
sathish()

#create variable inside function and same var name as global

d=14
O=12
b=1997
def guru():
    d=2
    O=6
    b=1997
    print("Guru D:O:B",d,O,b)
guru()
print("sathish D:O:B",d,O,b)

#global X

def amasaveni():
    global x
    x="sathish"
    
amasaveni()

print("Welocme Back" + x)
    
# function inside the gloable variable

x="raj"
def raj():
    global X
    x="ram"
raj()
print("Your are Correct" +  x)