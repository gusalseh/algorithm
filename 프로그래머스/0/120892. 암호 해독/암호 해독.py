def solution(cipher, code):
    answer = ''
    for idx in range(len(cipher)):
        if (idx+1)%code == 0:
            answer = answer+str(cipher[idx])
    return answer