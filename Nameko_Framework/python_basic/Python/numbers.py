#Numberic types int,float,complex
x=1 #int
y=2.3 #float
z=1j #complex
a=-1j #complex
print(type(x))
print(type(y))
print(type(z))
print(type(a))
#type conversion
x=1    #int
y=2.0  #float
z=1j+1   #complex

#convert into int to float
a=float(x)
#convert into float to int
b=int(y)
#convert into int to complex
c=complex(z)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))