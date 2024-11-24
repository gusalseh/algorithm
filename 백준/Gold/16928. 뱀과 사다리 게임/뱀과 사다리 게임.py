from collections import deque

N, M = map(int, input().split())

board = list(range(101))

for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v

visited = [False] * 101
queue = deque([(1, 0)])  # (현재 위치, 주사위 굴림 횟수)

while queue:
    position, rolls = queue.popleft()

    if position == 100:
        print(rolls)
        break

    for dice in range(1, 7):
        next_pos = position + dice
        if next_pos > 100:
            continue
        next_pos = board[next_pos]
        if not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, rolls + 1))
