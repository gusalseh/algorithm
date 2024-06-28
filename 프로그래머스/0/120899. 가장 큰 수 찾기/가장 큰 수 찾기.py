def solution(array):
    answer = []
    max_val = max(array)
    answer.append(max_val)
    
    for idx in range(len(array)):
        if array[idx] == max_val:
            answer.append(idx)
    
    return answer