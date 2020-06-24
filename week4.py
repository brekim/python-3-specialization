# week4

a = [1, 2, 3]
b = [2, 3, 4]

print(id(a))
print(id(b)) # Not the same ID!

a = b # Will make a an alias of b
print(a is b)

b = a[:]
print(b is a)
