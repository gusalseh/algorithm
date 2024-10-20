# 입력 받기
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
move_info = [tuple(map(int, input().split())) for _ in range(M)]

where_to_go = [
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1)
]

clouds_location = set([(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)])

for d, s in move_info:
    dx, dy = where_to_go[d - 1]

    new_clouds_location = set()
    for x, y in clouds_location:
        nx, ny = (x + dx * s) % N, (y + dy * s) % N
        new_clouds_location.add((nx, ny))

    for x, y in new_clouds_location:
        A[x][y] += 1

    disappeared_clouds_location = new_clouds_location
    clouds_location = set()

    from collections import defaultdict
    water_copy = defaultdict(int)
    for x, y in disappeared_clouds_location:
        count = 0
        for cx, cy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + cx, y + cy
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                count += 1
        A[x][y] += count

    for i in range(N):
        for j in range(N):
            if (i, j) in disappeared_clouds_location:
                continue
            if A[i][j] >= 2:
                clouds_location.add((i, j))
                A[i][j] -= 2

total_water = sum(map(sum, A))
print(total_water)
