def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    answer = 0
    n1 = 1
    n2 = 2
    for _ in range(n-2):
        n1, n2 = n2, n1+n2
        
    answer = n2 % 1234567
    return answer