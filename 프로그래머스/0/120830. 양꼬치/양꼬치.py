def solution(n, k):
    answer = 0
    service = n//10
    real_k = k - service
    answer = n*12000 + real_k*2000
    return answer