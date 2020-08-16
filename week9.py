# Author: Brett Kim

random_one_to_ten = [10, 5, 1, 6, 4, 7, 9, 3, 2, 8]

print(random_one_to_ten)
print(sorted(random_one_to_ten))
print(sorted(random_one_to_ten, reverse=True))

def absolute(x):
  if x >= 0:
    return x
  else:
    return -x

win_diff = [93, -3, -58, -3, 49, 10, 3, 48]
print(sorted(win_diff, reverse=True, key=absolute)
