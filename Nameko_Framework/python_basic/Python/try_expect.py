# Try and expect

try:
    print(x)
except:
    print("An Except occurred")

# try block does not raise an errors

try:
    print(x)
except:
    print("An Except occurred")
else:
    print("Nothing Went to Wrong")

# Finally Keywords
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
