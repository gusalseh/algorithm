N, K = map(int, input().split())
belt = list(map(int, input().split()))

robots = [False] * (2 * N)

stage = 0

while True:
    stage += 1

    belt.insert(0, belt.pop())
    robots.insert(0, robots.pop())

    if robots[N - 1]:
        robots[N - 1] = False

    for i in range(N - 2, -1, -1):
        if robots[i]:
            if not robots[i + 1] and belt[i + 1] > 0:
                robots[i] = False
                robots[i + 1] = True
                belt[i + 1] -= 1
                if i + 1 == N - 1:
                    robots[i + 1] = False

    if belt[0] > 0 and not robots[0]:
        robots[0] = True
        belt[0] -= 1

    if robots[N - 1]:
        robots[N - 1] = False

    zero_count = belt.count(0)
    if zero_count >= K:
        break

print(stage)