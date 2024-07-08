def solution(s):
    answer = True
    cnt = 0
    
    for i in s:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
            
        if cnt < 0:
            answer = False
            break
        elif cnt == 0:
            answer = True
        else:
            answer = False

    return answer