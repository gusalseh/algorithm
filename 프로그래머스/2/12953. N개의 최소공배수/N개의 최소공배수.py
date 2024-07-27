def solution(arr):
    answer = 1
    gcd = 0
    
    for i in range(len(arr)):
        if i == 0:
            continue
        else:
            a = arr[i-1]
            b = arr[i]
            while b:
                a, b = b, a%b
            gcd = a
        answer = arr[i-1] * arr[i] // gcd
        arr[i] = answer
    
    return answer