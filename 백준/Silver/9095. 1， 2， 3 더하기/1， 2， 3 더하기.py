N = int(input())
inputs = []
for _ in range(N):
    inputs.append(int(input()))

def triple_pivo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n ==3:
        return 4
    else:
        pivo_list = [1,2,4]
        for i in range(n):
            if i in [0,1,2]:
                continue
            else:
                new = pivo_list[i-3] + pivo_list[i-2] + pivo_list[i-1]
                pivo_list.append(new)
        return pivo_list[-1]

for j in inputs:
    print(triple_pivo(j))