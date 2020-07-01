# week5.py

# Reading
file = open(".\\check.txt", "r")
content = file.readlines()
print(content)

for line in file:
    print(line.strip())

file.close()

# Writing
file = open(".\\check.txt", "a") # w to change it

file.write("\nExample,Country,0,0,0.0,1.05")

file.close()

# Using with to open Python files
with open('check.txt') as new_file:
    lines = new_file.readlines()
    for line in lines:
        sp = line.split(",")
        print("{} - {}. Rating: {} K: {} D: {} ADR: {}".format(sp[0], sp[1], sp[5], sp[2], sp[3], sp[4]))