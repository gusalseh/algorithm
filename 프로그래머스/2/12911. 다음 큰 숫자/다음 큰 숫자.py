def solution(n):
    answer = 0
    original = n
    list = []
    bin_result = ""
    while n:
        list.append(str(n%2))
        n=n//2
    list.reverse()
    for i in list:
        bin_result += i
    cnt_n = bin_result.count("1")
    
    check_num = original+1
    original_check_num = original+1
    while True:
        list2 = []
        bin_result2 = ""
        while check_num:
            list2.append(str(check_num%2))
            check_num=check_num//2
        list2.reverse()
        for i in list2:
            bin_result2 += i

        if bin_result2.count("1") == cnt_n:
            answer = original_check_num
            break
        check_num = original_check_num + 1
        original_check_num += 1
    return answer