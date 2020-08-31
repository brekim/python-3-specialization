# Author - Brett Kim

import copy as cp

mavs = [[33, 42], [5, 1], [42, 4]]

for lst in mavs:
    for score in lst:
        print(score)

rockets = {'players':
            {'name': 'James Harden',
            'points': 40,
            'assists': 8,
            'rebounds': 6,
            'physical_features': {'beard': True,
                                    'bald': False}
            }
        }

print(rockets['players']['points'])

malta = {'events':
            {
            2019: {'name': 'ESL Cologne',
            'winner': 'Astralis'
            },
            2020: {'name': 'ELEAGUE Boston',
            'winner': 'Cloud9',
            'runnerup': 'FaZe'}
            }
        }

print(malta['events'][2019]['winner'])
print(malta['events'][2020]['winner'])

scores = [[1, 2, 3], [4, 3, 2]]

for ind_scores in scores:
    print("You can count on me, like")

    for score in ind_scores:
        print(score)
        
    print("I'll be there")

scores = [1, 2, ['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]

for x in scores:
    print("level1: ")

    if type(x) is list:
        for y in x:
            print("\tlevel 2: {}".format(y))
    else:
        print(x)

genre = [['dancehall', 'indie_pop'], ['singer_songwriter', 'aboriginal']]

shallow_copy = genre[:]
deep_copy = cp.deepcopy(shallow_copy)


nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

output = nested[1][2]


lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = 'yellow' in lst[2]

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four = 4 in lst[1]

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = 'orange' in lst[0]


L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = 'hola' in L

# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = [5, 8, 7] in L

# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = 6.6 in L[2]


nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
if 'data' in nested:
    data = True
else:
    data = False

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.

if 24 in nested:
    twentyfour = True
else:
    twentyfour = False

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
if 'whole' in nested:
    whole = True
else:
    whole = False

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
if 'physics' in nested:
    physics = True
else:
    physics = False


nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

london_gold = nested_d['London']['Great Britain']

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]

# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']

# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][3]


nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []

for event in nested_d:
    for country in nested_d[event]:
        if 'USA' == country:
            US_count.append(nested_d[event]['USA'])


l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = []

for list in l_of_l:
    third.append(list[2])

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = []
other = []

for group in athletes:
    for athlete in group:
        if 't' in athlete:
            t.append(athlete)
        else:
            other.append(athlete)