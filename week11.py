# week11.py

def triple(x):
    return x*3

dancing = [1, 2, 3, 4]
cool_dancing = map(triple, dancing)

for num in cool_dancing:
    print(num)