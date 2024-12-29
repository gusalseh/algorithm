gears = [list(map(int, list(input()))) for _ in range(4)]

K = int(input())

for _ in range(K):
    gear_num, direction = map(int, input().split())
    gear_idx = gear_num - 1

    directions = [0, 0, 0, 0]
    directions[gear_idx] = direction

    tmp_dir = direction
    for i in range(gear_idx - 1, -1, -1):
        if gears[i][2] != gears[i + 1][6]:
            tmp_dir = -tmp_dir
            directions[i] = tmp_dir
        else:
            break

    tmp_dir = direction
    for i in range(gear_idx + 1, 4):
        if gears[i][6] != gears[i - 1][2]:
            tmp_dir = -tmp_dir
            directions[i] = tmp_dir
        else:
            break

    for i in range(4):
        if directions[i] == 0:
            continue
        elif directions[i] == 1:
            gears[i].insert(0, gears[i].pop())
        elif directions[i] == -1:
            gears[i].append(gears[i].pop(0))

score = 0
if gears[0][0] == 1:
    score += 1
if gears[1][0] == 1:
    score += 2
if gears[2][0] == 1:
    score += 4
if gears[3][0] == 1:
    score += 8

print(score)