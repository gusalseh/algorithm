def solution(n):
    answer = []
    if n%2==0:
        for i in range(0,(n//2)):
            answer.append(2*i+1)
    else:
        for j in range(0,((n+1)//2)):
            answer.append(2*j+1)
    return answer