a, b, c = map(int, input().split())

remain = a % c
result = 1

while b > 0:
    if b % 2 == 1:
        result = (result * remain) % c
    b //= 2
    remain = (remain * remain) % c

print(result)
