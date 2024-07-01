def solution(num_list):
    mul_val = 1
    pul_val = 0
    answer = 0
    for i in num_list:
        mul_val *= i
        pul_val += i
    if mul_val < pul_val**2:
        answer = 1
    else:
        answer = 0
    return answer