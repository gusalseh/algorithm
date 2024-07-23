N = int(input())
inputs = []
for _ in range(N):
    inputs.append(int(input()))

def pivo(n, target_num):
    if target_num == 0:
        if n == 1:
            return 0
        elif n== 0 or n == 2 or n == 3:
            return 1
        elif n == 4:
            return 2
        else:
            n1 = 1
            n2 = 2
            for _ in range(n-2-2):
                n1, n2 = n2, n1 + n2
            return n2
    else:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            n1 = 1
            n2 = 2
            for _ in range(n-2-1):
                n1, n2 = n2, n1 + n2
            return n2

for i in inputs:
    pivo0 = pivo(i, 0)
    pivo1 = pivo(i, 1)

    print(f"{pivo0} {pivo1}")