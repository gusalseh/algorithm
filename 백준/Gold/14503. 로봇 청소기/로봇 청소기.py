N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cleaned_room = 0

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cleaned_room += 1

    clean_possible = False
    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = r + dx[d], c + dy[d]

        if room[nx][ny] == 0:
            r, c = nx, ny
            clean_possible = True
            break

    if not clean_possible:
        nx, ny = r - dx[d], c - dy[d]
        if room[nx][ny] == 1:
            break
        r, c = nx, ny

print(cleaned_room)