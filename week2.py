s = "This is a string..."
m = """This is
a multi
-
line
string"""

print(s)
print(str(len(m)))

players = ["SicK", "dapr"]
print("Players on Sentinels: " + str(len(players)))

username = "Shake"
firstLetterInUsername = username[0]
print(firstLetterInUsername)
lastLetterInUsername = username[len(username) - 1]
print(lastLetterInUsername)

players = ["device", "s1mple", "mertz"]
mouz2018 = ["sunNy", "ropz", "chrisJ", "oskar", "STYKO"]

print(mouz2018[:2])
print(mouz2018[2:])
print(mouz2018 * 5)

print("I guess we're getting rid of the " + str(mouz2018.index("sunNy") + 1) + "st player on the team.")

allPlayers = players + mouz2018
print(allPlayers)

allMouzPlayers = '<3'.join(mouz2018)
print(allMouzPlayers)