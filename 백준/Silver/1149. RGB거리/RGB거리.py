N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

rgb_compare = [[0] * 3 for _ in range(N)]

rgb_compare[0][0] = cost[0][0]
rgb_compare[0][1] = cost[0][1]
rgb_compare[0][2] = cost[0][2]

# 두 번째 집부터 마지막 집까지
for i in range(1, N):
    rgb_compare[i][0] = min(rgb_compare[i-1][1], rgb_compare[i-1][2]) + cost[i][0]  # 빨강으로 칠할 경우
    rgb_compare[i][1] = min(rgb_compare[i-1][0], rgb_compare[i-1][2]) + cost[i][1]  # 초록으로 칠할 경우
    rgb_compare[i][2] = min(rgb_compare[i-1][0], rgb_compare[i-1][1]) + cost[i][2]  # 파랑으로 칠할 경우

print(min(rgb_compare[N-1][0], rgb_compare[N-1][1], rgb_compare[N-1][2]))