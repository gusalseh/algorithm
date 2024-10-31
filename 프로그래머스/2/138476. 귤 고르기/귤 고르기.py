def solution(k, tangerine):
    answer = 0
    tan_dic = {}
    
    for i in tangerine:
        if i not in tan_dic:
            tan_dic[i] = 1
        else:
            count = tan_dic[i]
            tan_dic[i] = count + 1
            
    value_list = sorted(list(tan_dic.values()), reverse=True)
    
    total = 0
    
    for j in value_list:
        total += j
        answer += 1
        if total >= k:
            break
    
    return answer