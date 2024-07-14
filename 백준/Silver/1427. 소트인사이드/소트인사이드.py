n = str(input())
int_list = []

for i in n:
    int_list.append(int(i))

int_list.sort(reverse=True)

for i in int_list:
    print(str(i), end='')