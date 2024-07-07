def solution(n, m):
    answer = []
    pre_csg = n*m
    while m:
        n, m = m, n%m
    cdg=n
    csg=pre_csg//n
    answer = [cdg, csg]
    return answer