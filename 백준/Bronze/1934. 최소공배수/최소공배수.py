def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

N = int(input())
lines = []
for _ in range(N):
    nums = list(map(int, input().split()))
    lines.append(nums)

for i in range(len(lines)):
    a, b = lines[i]
    lcm_ab = lcm(a, b)
    print(lcm_ab)