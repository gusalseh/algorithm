def solution(s):
    answer = []
    cnt_one = 0
    answer_1 = 0
    answer_2 = []
    while True:
        if s == "1":
            break
        for i in s:
            if i == "1":
                cnt_one += 1
        answer_1 += len(s) - cnt_one
        result = []
        result_string = ""
        while (cnt_one):
            result.append(cnt_one % 2)
            cnt_one //= 2
        result.reverse()
        for i in result:
            result_string += str(i)
        answer_2.append(result_string)
        s=result_string
        
    answer = [len(answer_2),answer_1]
    return answer