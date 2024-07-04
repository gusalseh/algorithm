N = int(input())
input_list = list(map(int, input().split()))

M = max(input_list)
answer = sum(input_list)*100/(N*M)
print(answer)