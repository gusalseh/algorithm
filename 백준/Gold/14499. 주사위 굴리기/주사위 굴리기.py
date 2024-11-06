N, M, x, y, K = map(int, input().split())
map_shape = [list(map(int, input().split())) for _ in range(N)]
move_direction = list(map(int, input().split()))

# 동 서 남 북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0] * 6


for direction in move_direction:
    X, Y = x + dx[direction-1], y + dy[direction-1]

    if X < 0 or X >= N or Y < 0 or Y >= M:
        continue

    if direction == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif direction == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif direction == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0],  dice[5], dice[1]
    elif direction == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if map_shape[X][Y] == 0:
        map_shape[X][Y] = dice[5]
    else:
        dice[5] = map_shape[X][Y]
        map_shape[X][Y] = 0

    x, y = X, Y

    print(dice[0])