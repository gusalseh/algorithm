N, M = map(int,input().split())
# 첫번째 라운드 실시간 순위(각 인덱스는 선수 넘버)
initial_round = []
# 마지막 라운드 실시간 순위(각 인덱스는 선수 넘버)
final_round = []
for _ in range(N):
    value = int(input())
    initial_round.append(value)
for _ in range(M):
    value = int(input())
    final_round.append(value)

# 첫번쨰 라운드 최종 순위
ir_result = [ 0 for _ in range(N)]
# 마지막 라운드 최종 순위
fr_result = []

for i in range(len(initial_round)):
    ir_result.insert(initial_round[i]-1,i+1)
    ir_result.pop()

# 마지막 라운드 경기 순서
fr_start = ir_result[:M]
fr_start.reverse()

for j in range(len(final_round)):
    fr_result.insert(final_round[j]-1,fr_start[j])

for i in range(3):
    print(fr_result[i])
