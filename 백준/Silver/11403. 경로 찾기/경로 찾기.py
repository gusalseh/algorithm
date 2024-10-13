N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for x in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][x] and graph[x][j]:
                graph[i][j] = 1

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()