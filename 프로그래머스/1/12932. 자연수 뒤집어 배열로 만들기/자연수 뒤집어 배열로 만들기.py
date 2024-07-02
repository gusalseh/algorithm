def solution(n):
    answer = []
    length = len(str(n))
    for i in range(length,0,-1):
        val = str(n)[i-1]
        answer.append(int(val))
    return answer