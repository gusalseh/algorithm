def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i].isupper() == True:
            answer = my_string[:i]+my_string[i].lower()+my_string[i+1:]
            my_string = answer
        else:
            answer = my_string[:i]+my_string[i].upper()+my_string[i+1:]
            my_string = answer
    return answer