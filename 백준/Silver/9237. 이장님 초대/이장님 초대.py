n = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
d_day = []

for i in range(len(trees)):
    d_day.append(trees[i]+i+1)

print(max(d_day)+1)