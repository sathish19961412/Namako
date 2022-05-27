#assign String to variable
a="sathish"
print(a)

#Multilines strings
b="""
It is a long established fact that a reader will be distracted by the readable content of a page 
when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal 
distribution of letters, as opposed to using 'Content here, content here', making it look like 
readable English. 
"""
print(b)

#String are Arrays
a="sathish"
print(a[1])

#looping throught the string
for x in a:
    print(x)
    
#String Length
a="guruprasath"
print(len(a))

#check string
txt="the best things is a life free"
print("free" in txt)

#check if condition
txt1="sathish"
if "sathish" in txt1:
    print("yes,'sathish' is present")
else:
    for x in txt1:
        print(x)
        
#check if not
txt2="sathish"
if "sathish1" not in txt2:
    print("No,'sathish' is not present")
else:
    print("yes,'sathish' is present")