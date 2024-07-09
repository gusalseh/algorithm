def solution(n, arr1, arr2):
    answer = []
    arr_1 = []
    arr_2 = []
    
    for i in arr1:
        two_list = []
        two_dim = ""
        while i:
            two_list.append(i%2)
            i = i // 2
        # n자리에 맞게 0의 숫자를 채워주는 과정
        while len(two_list)!=n:
            two_list.append(0)
        two_list.reverse()
        for i in two_list:
            two_dim += str(i)
        arr_1.append(two_dim)
        
    for j in arr2:
        two_list = []
        two_dim = ""
        while j:
            two_list.append(j%2)
            j = j // 2
        while len(two_list)!=n:
            two_list.append(0)
        two_list.reverse()
        for j in two_list:
            two_dim += str(j)
        arr_2.append(two_dim)
    
    for k in range(n):
        temp = ""
        for l in range(n):
            if arr_1[k][l] == arr_2[k][l] == "0":
                temp += " "
            else:
                temp += "#"
        answer.append(temp)
    return answer