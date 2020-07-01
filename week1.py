# hello.py

import random

# Print statements, comments, values, and data types
print("Hello World")

print(2 + 2)
print(2 * 2)
print(18 % 4)

almonds = 42
elective = "Interpret Dance Using Python 3"

print(type(elective))
print(type(str(almonds)))

print("Yes, this is it! " + str(almonds) + " almonds!")

a = 6
b = a

a += 2

print(a) # Should be 8
print(b) # Should be 6

# n = input("Yellow, Colonel Mustard")
# print("Hello", n)

rice = 0
for i in range(3):
    rice += i
    print(str(i) + ": " + str(rice))

potato = random.randrange(1, 3)
print(potato)