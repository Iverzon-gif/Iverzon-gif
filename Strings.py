# Strings

# We have already covered strings, integers, float, booleans and list

# Integers, float, and booleans are all considered to be simple data types
# They cannot be broken down!

# List and strings are different! They are made up of samaller pieces which
# CAN be broken down

# We already know what strings are!
print("hello world")
print(type("hello world"))

# Operation on strings
# Addition sign concatenation
Greeting = "Hello "
Name = "Iverzon"
print(Greeting + Name)

# * Operator
print(Greeting*3)
print(Greeting + Name*3)
print((Greeting + Name)*3)

# Index Operator
name = "Iver"
print(name[2])
print(name[0] + name[3])

# Slicing strings
print(name[0:2])
print(name[:2])
print(name[2:])

#Lowercase and Uppercase
name ="Iverzon"
print(name.lower())
print(name.upper())

# Count how many times a characte appears in a strinh
print(name.count("i"))

# Replace specific characters with other characters
print(name.replace("i", "m"))
name = "iverzon"
New_name = name.replace("i", "m")
print(New_name)

# Finding the length of a string
print(len(name))

# Format string
#your_name = input("Your name: ")
#hello = "Hello {}".format(your_name)
#print(hello)

# Each letter in python is assigned to a specific number!
print("orange" < "strawberry")
print(ord("o"))
print(chr(78))
# We can perform math on a string

# in and not operators
fruit = "banana"
print("a" in fruit)
print("s" not in fruit)

# Incorporate a few things we've learnt so far
x = "hello"
y = ""
for character in x:
    y = character.upper() + y
print(y)