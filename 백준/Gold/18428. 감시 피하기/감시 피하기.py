N = int(input())
hallway = [input().split() for _ in range(N)]

teachers = []
empty_spaces = []
for i in range(N):
    for j in range(N):
        if hallway[i][j] == 'T':
            teachers.append((i, j))
        elif hallway[i][j] == 'X':
            empty_spaces.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

found = False

for i in range(len(empty_spaces)):
    for j in range(i + 1, len(empty_spaces)):
        for k in range(j + 1, len(empty_spaces)):
            x1, y1 = empty_spaces[i]
            x2, y2 = empty_spaces[j]
            x3, y3 = empty_spaces[k]
            hallway[x1][y1] = 'O'
            hallway[x2][y2] = 'O'
            hallway[x3][y3] = 'O'

            check = True
            for tx, ty in teachers:
                for d in range(4):
                    nx, ny = tx, ty
                    while 0 <= nx < N and 0 <= ny < N:
                        if hallway[nx][ny] == 'O':
                            break
                        if hallway[nx][ny] == 'S':
                            check = False
                            break
                        nx += dx[d]
                        ny += dy[d]
                    if not check:
                        break
                if not check:
                    break

            if check:
                found = True
                break

            hallway[x1][y1] = 'X'
            hallway[x2][y2] = 'X'
            hallway[x3][y3] = 'X'

        if found:
            break
    if found:
        break

if found:
    print("YES")
else:
    print("NO")