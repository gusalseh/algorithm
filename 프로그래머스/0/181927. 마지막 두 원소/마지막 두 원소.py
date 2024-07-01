def solution(num_list):
    if num_list[-1] > num_list[-2]:
        add = num_list[-1] - num_list[-2]
        num_list.append(add)
    else:
        num_list.append(num_list[-1]*2)
    return num_list