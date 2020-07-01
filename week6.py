# week6.py

players = {}
players['dapr'] = 1080
players['dazzLe'] = 944
players['Relyks'] = 800
print(players)

if 'dazzLe' in players:
    print("We have a cool team featuring the talents of dazzLe!")

medals = {'gold': 33, 'silver': 17, 'bronze': 12}
print(medals)

del players['Relyks']
print(players)

for key in medals.keys():
    print(key, "has the value", medals[key])

print(list(medals.keys()))
print(list(medals.values()))

# Alias
new_identity = players
print(new_identity is players)

# Copy
singularity = players.copy()
print(singularity is players)

# Working with accumulator dictionaries
workout_days = {'Monday': 23, 'Tuesday': 3, 'Wednesday': 8, 'Thursday': 7, 'Friday': 44, 'Saturday': 42, 'Sunday': 2}

num_days = 0
for key in workout_days.keys():
    num_days += workout_days[key]
print("Number of days:", num_days)

smallest_key = ""
for key in workout_days.keys():
    if workout_days[key] < workout_days.get(smallest_key, 9999999999999):
        smallest_key = key
print(smallest_key)