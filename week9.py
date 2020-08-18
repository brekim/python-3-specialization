# Author: Brett Kim

random_one_to_ten = [10, 5, 1, 6, 4, 7, 9, 3, 2, 8]

print(random_one_to_ten)
print(sorted(random_one_to_ten))
print(sorted(random_one_to_ten, reverse=True))

lett = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(lett, reverse=True)

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals.keys())


medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

med_sort = sorted(medals, key=lambda k: medals[k], reverse=True)

top_three = []

top_three.append(med_sort[0])
top_three.append(med_sort[1])
top_three.append(med_sort[2])


groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries.keys(), key=lambda k: groceries[k], reverse=True)

def last_four(id):
    id = str(id)
    return id[-1:-4]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key=last_four)


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key=lambda k: str(k)[-4:-1])


ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key=lambda k: str(k)[1])