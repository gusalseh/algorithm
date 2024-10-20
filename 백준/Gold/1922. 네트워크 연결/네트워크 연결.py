n = int(input())
m = int(input())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent_nodes = [i for i in range(n + 1)]

total_cost = 0

for cost, a, b in edges:
    x = a
    while parent_nodes[x] != x:
        x = parent_nodes[x]
    x_root = x

    y = b
    while parent_nodes[y] != y:
        y = parent_nodes[y]
    y_root = y

    if x_root != y_root:
        parent_nodes[y_root] = x_root
        total_cost += cost

print(total_cost)
