def solution(n):
    answer = 0
    max_length = 0
    cnt = 0
    while True:
        if (cnt*(cnt+1)//2) >= n:
            max_length = cnt
            break
        else:
            cnt += 1
    for i in range(1,max_length+1):
        if i%2 == 1:
            if n%i == 0:
                answer += 1
        else:
            if n%i == (i//2):
                answer += 1
    return answer