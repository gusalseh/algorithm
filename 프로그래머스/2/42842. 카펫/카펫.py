def solution(brown, yellow):
    answer = [0, 0]
    
    answer[0] = (brown + 4 - ((brown-4)**2 - 16*yellow)**0.5)/4
    answer[1] = (brown + yellow) / answer[0]
    
    if answer[0] < answer[1]:
        answer[0], answer[1] = answer[1], answer[0]
    
    return answer