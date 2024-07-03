def solution(s):
    answer = ''
    a = list(map(int,s.split()))
    max_val = max(a)
    min_val = min(a)
    answer = f'{min_val} {max_val}'
    return answer