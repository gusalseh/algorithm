t = int(input())
num_list = []

for _ in range(t):
    count = int(input())
    group = [input() for _ in range(count)]
    num = sorted(group)
    answer = True
    for i in range(count - 1):
        if num[i + 1].startswith(num[i]):
            answer = False
            break
    if answer:
        print('YES')
    else:
        print('NO')