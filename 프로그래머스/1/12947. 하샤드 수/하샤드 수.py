def solution(x):
    answer = True
    value = 0
    for i in str(x):
        value += int(i)
    if x%value == 0:
        answer = True
    else:
        answer = False
    return answer