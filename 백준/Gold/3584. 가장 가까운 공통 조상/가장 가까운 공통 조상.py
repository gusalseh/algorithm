T = int(input())
result = []

for _ in range(T):
    N = int(input())

    parent = [-1] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a

    target_node1, target_node2 = map(int, input().split())

    ancestors1 = set()
    while target_node1 != -1:
        ancestors1.add(target_node1)
        target_node1 = parent[target_node1]
        
    common_node = -1
    while target_node2 != -1:
        if target_node2 in ancestors1:
            common_node = target_node2
            break
        target_node2 = parent[target_node2]

    result.append(common_node)

for i in result:
    print(i)
