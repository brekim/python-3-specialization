# week11.py

def triple(x):
    return x*3

dancing = [1, 2, 3, 4]
cool_dancing = map(triple, dancing)

for num in cool_dancing:
    print(num)

def keep_evens(x):
    if x % 2 == 0:
        return True
    else:
        return False

x = filter(keep_evens, dancing)

for num in x:
    print(num)

prancing = [1, 2, 3, 4]
cool_dance = [value * 2 for value in prancing]

for num in cool_dance:
    print("Num: " + str(num))