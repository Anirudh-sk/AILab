from collections import defaultdict
import random
room = defaultdict(list)
gold = 1
wumpus = 1
pit = 1
flag = 1
print(room)
while (wumpus):
    p = random.randint(0, 3)
    q = random.randint(0, 3)
    pq = str(p)+','+str(q)
    if (room[pq] == 'Pit' or room[pq] == 'Gold' or (p == 0 and q == 0)):
        print(pq, room[pq], "contine")
        continue
    if (pit):
        room[pq].append('Pit')
        if (p < 3):
            pq = str(p+1)+','+str(q)
            room[pq].append('Breeze')
        if (p > 0):
            pq = str(p-1)+','+str(q)
            room[pq].append('Breeze')
        if (q < 3):
            pq = str(p)+','+str(q+1)
            room[pq].append('Breeze')
        if (q > 0):
            pq = str(p)+','+str(q-1)
            room[pq].append('Breeze')
        pit -= 1

    elif (gold):
        room[pq].append('Gold')
        gold -= 1
    else:
        room[pq].append('Wumpus')
        if (p < 3):
            pq = str(p+1)+','+str(q)
            room[pq].append('Stench')
        if (p > 0):
            pq = str(p-1)+','+str(q)
            room[pq].append('Stench')
        if (q < 3):
            pq = str(p)+','+str(q+1)
            room[pq].append('Stench')
        if (q > 0):
            pq = str(p)+','+str(q-1)
            room[pq].append('Stench')
        wumpus -= 1
print(room)
score = 0
p = 0
q = 0
while (flag):
    print("Current position:", p, ",", q)
    print("""1. Move Left
2. Move Right
3. Move Up
4. Move Down""")

    move = int(input(":"))

    match move:
        case 1:
            q -= 1
        case 2:
            q += 1
        case 3:
            p -= 1
        case 4:
            p += 1
        case _:
            print("Invalid move, please enter from 1-4")

    currentRoom = room[str(p)+','+str(q)]
    print("Room:", room[str(p)+','+str(q)])
    score -= 15
    if "Gold" in currentRoom:
        score += 5000
        result = "Win"
        flag = 0
        print("You Won, you found the GOLD")
    if "Wumpus" in currentRoom or "Pit" in currentRoom:
        score -= 5000
        result = "Lost"
        flag = 0
        print("You Lost, Wumpus kitta matikita")
    print("Score:", score)
