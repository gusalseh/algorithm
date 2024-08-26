from collections import deque

def find_parents(n, edges):
    # 그래프 초기화
    graph = [[] for _ in range(n+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # 부모 노드를 저장할 리스트
    parents = [0] * (n+1)
    
    # BFS 수행
    queue = deque([1])  # 루트 노드부터 시작
    visited = [False] * (n+1)
    visited[1] = True
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                parents[neighbor] = current
                visited[neighbor] = True
                queue.append(neighbor)
    
    # 결과 반환
    return parents[2:]  # 2번 노드부터의 부모 노드 반환

# 입력 처리
n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]

# 부모 노드 찾기
result = find_parents(n, edges)

# 결과 출력
for parent in result:
    print(parent)