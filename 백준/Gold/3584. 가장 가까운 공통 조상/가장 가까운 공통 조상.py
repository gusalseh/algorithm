def path_to_root(node, parent):
    path = []
    while node != -1:
        path.append(node)
        node = parent[node]
    return path


T = int(input())
result = []

for _ in range(T):
    N = int(input())

    parent = [-1] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a

    target_node1, target_node2 = map(int, input().split())

    path1 = path_to_root(target_node1, parent)
    path2 = path_to_root(target_node2, parent)

    common_node = -1
    path1_set = set(path1)
    for node in path2:
        if node in path1_set:
            common_node = node
            break

    result.append(common_node)

for i in result:
    print(i)
