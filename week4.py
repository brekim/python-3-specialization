# week4

a = [1, 2, 3]
b = [2, 3, 4]

print(id(a))
print(id(b)) # Not the same ID!

a = b # Will make a an alias of b
print(a is b)

b = a[:]
print(b is a)

dance = "DANCER"
print("Hello {}!".format(dance))

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

scores3 = scores.split(" ")

a_scores = 0

for score in scores3:
    if int(score) >= 90:
        a_scores += 1

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

orgs = sent.split()
acro = []

for org in orgs:
    word = False
    
    for stopword in stopwords:
        if (org == stopword):
            word = True
            
    if word == False:
        b = str(org[0] + org[1])
        acro += [b]
        print(b)

print(acro)
acro = ". ".join(acro)
print(acro)

p_phrase = "was it a car or a cat I saw"

c = []

for p in p_phrase:
    c += [p]

c.reverse()
r_phrase = "".join(c)

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for string in inventory:
    a = string.split(", ")
    print("The store has {} {}, each for {} USD.".format(a[1], a[0], a[2]))