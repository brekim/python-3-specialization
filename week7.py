def hello(name, count):
    greeting = "Hello {}!\n".format(name)
    print(greeting*count)

def square(number):
    return number * number

hello("Wendy", square(3))

def sum_of_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

br = [2, 4, 6, 8]
print(sum_of_list(br))