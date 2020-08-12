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