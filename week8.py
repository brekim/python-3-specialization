# Author: Brett Kim

it = 0
while it <= 10:
    print(it)
    it += 1

hp = 10
enemyHP = 10
atk = 3
enemyATK = 1

while hp > 0:
    hp -= enemyATK
    if hp <= 0:
        break
    print("HP: " + str(hp))
    print("Enemy HP: " + str(enemyHP))
    
    enemyHP -= atk
    if enemyHP <= 0:
        break
    print("HP: " + str(hp))
    print("Enemy HP: " + str(enemyHP))

def opt_par(x, y = 3):
    return x * y

print(opt_par("Ok"))

def opt_par_ii(x = 4, y = 9, z = 21):
    return x * y / z

print(opt_par_ii(z = 4))

f = lambda x: x - 2
print(f(2))