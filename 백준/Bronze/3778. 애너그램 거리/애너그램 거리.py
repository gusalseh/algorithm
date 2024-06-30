N = int(input())
lines = []
for _ in range(N*2):
    lines.append(input().strip())

# lines=['pneumonoultramicroscopicsilicovolcanoconiosis','pop']

for i in range(0, len(lines), 2):
    a=lines[i]
    b=lines[i+1]

    length_1 = len(a)
    length_2 = len(b)
    count = 0

    for j in range(len(a)):
        for k in range(len(b)):
            if a[j] == b[k]:
                b=b[:k]+b[k+1:]
                count += 1
                break
    print(f'Case #{(i+2)//2}:',length_1 + length_2 - count * 2)