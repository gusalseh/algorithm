def solution(s):
    str_list = []
    for i in range(len(s)):
        str_list.append(s[i])
        temp_idx = len(str_list)-1
        if len(str_list)>1 and str_list[temp_idx] == str_list[temp_idx-1]:
            str_list.pop()
            str_list.pop()

    if len(str_list) == 0:
        return 1
    else:
        return 0