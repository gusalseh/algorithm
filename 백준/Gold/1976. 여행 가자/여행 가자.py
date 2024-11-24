N = int(input())
M = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 모든 도시에서 자기 자신으로의 경로를 1로 설정
for i in range(N):
    graph[i][i] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

plan = list(map(int, input().split()))
# 도시 번호를 0부터 시작하도록 인덱스 조정
plan = [city - 1 for city in plan]

possible = True
for i in range(len(plan) - 1):
    if not graph[plan[i]][plan[i + 1]]:
        possible = False
        break

if possible:
    print("YES")
else:
    print("NO")
