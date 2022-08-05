# Booleans

print(True)
print("True")

print(type(True))  # The type is a bool
print(type("True")) # The type is a string

# Testing wether these statement are correct
print(5 == 5)
print(6 == 5)

# Incorporating then if statement with a boolean
x = 11
y = 5
if x % y == 0:
    print(True)
else:
    print(False)

# while loop
#number =  1
#while number < 4:
#   print(number)
#   if number == 4:
#       break
#   number = number + 1

# incoporating the else statement within the while loop
number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print("number is no longer less than 4")


# If satement
number = 1
if number > 1:
    print("Positive Numbe Greater Than One")
elif number == 0:
    print("Zero")
elif number == 1:
    print("One")
else:
    print("Negative Number")
