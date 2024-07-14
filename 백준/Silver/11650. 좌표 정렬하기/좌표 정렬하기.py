N = int(input())
lists = []

for _ in range(N):
    a,b = map(int,input().split())
    lists.append((a,b))

lists.sort()

# 결과 출력하기
for val in lists:
    print(val[0], val[1])