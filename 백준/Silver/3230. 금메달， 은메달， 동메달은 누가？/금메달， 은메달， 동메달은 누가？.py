N, M = map(int,input().split())
initial_round = []
final_round = []
for _ in range(N):
    value = int(input())
    initial_round.append(value)
for _ in range(M):
    value = int(input())
    final_round.append(value)

ir_result = [ 0 for _ in range(N)]
answer = []

for i in range(len(initial_round)):
    ir_result.insert(initial_round[i]-1,i+1)
    ir_result.pop()
# print(ir_result)

fr_result = ir_result[:M]
fr_result.reverse()
# print(fr_result)

for j in range(len(final_round)):
    answer.insert(final_round[j]-1,fr_result[j])

# print(answer)

print(answer[0])
print(answer[1])
print(answer[2])