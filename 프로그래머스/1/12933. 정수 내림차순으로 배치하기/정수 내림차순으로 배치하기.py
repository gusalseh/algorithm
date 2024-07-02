def solution(n):
    answer = ''
    asc = []
    for i in str(n):
        asc.append(int(i))
    asc.sort()
    asc.reverse()
    for j in asc:
        answer += str(j)
    return int(answer)