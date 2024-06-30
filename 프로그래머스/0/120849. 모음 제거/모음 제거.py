def solution(my_string):
    answer = ''
    target=['a','e','i','o','u']
    for i in target:
        answer = my_string.replace(i,"")
        my_string = answer
    return answer