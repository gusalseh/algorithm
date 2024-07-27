def solution(numer1, denom1, numer2, denom2):
    answer = []
    ans_num = (numer1 * denom2) + (numer2 * denom1)
    ans_den = (denom1 * denom2)
    answer.append(ans_num)
    answer.append(ans_den)
    
    a = max(answer)
    b = min(answer)
    while b>0:
        a, b = b, a%b
    
    return [answer[0]/a, answer[1]/a]