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