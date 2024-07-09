def solution(arr, n):
    if len(arr)%2==1:
        for i in range(len(arr)):
            if i%2==0:
                arr[i]+=n
    else:
        for j in range(len(arr)):
            if j%2==1:
                arr[j]+=n
    return arr