N = int(input())
lines = []
for _ in range(N):
    nums=list(map(int,input().split()))
    lines.append(nums)

for i in range(len(lines)):
    a,b=lines[i]
    result = 0
    gcd=0
    while b:
        a, b = b, a % b
        gcd=a
    result = lines[i][0]*lines[i][1] // gcd
    print(result)
