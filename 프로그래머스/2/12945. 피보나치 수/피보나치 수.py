def solution(n):
    answer = 0
    num_list = [0,1]
    for i in range(2, n+1):
        num_list.append(num_list[i-1] + num_list[i-2])
    answer = num_list[-1]%1234567
    return answer