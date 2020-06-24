# week3.py

print(8 <= 5)
print(4 > 3)

x = 4
print(x > -3 or x < 5)
print(x < 3 and x > 5)
print(not (x > -3 or x < 5))

print("a" not in ["Deathconsciousness", "KIDS SEE GHOSTS", "Madvillainy", "Triple Baka"])

if (4 == 4):
    print("4 EQUALS 4?!")
else:
    print("Math machine broke")

if(x > 8):
    print("This is a big number. Now we're talking.")

y = 5

if y == 4:
    print("Kasane")
elif y == 5:
    print("Teto")
else:
    print("I don't know what you're talking about.")

talk = "Time to dance in my disco pants"

x = 0
for char in talk:
    if char in ['a', 'e', 'i', 'o', 'u']:
        x += 1
print("The number of vowels are " + str(x) + "!")

num = [1, 2, 3, 999, 4, 5]
largest_num = num[0]

for number in num:
    if number > largest_num:
        largest_num = number
print(largest_num)