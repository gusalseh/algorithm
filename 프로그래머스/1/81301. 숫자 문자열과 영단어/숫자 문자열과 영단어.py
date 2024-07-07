def solution(s):
    # dic = {"0":"zero","1":"one", "2":"two", "3":"three", "4":"four",
    #       "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
    dic = {"zero":"0","one":"1", "two":"2", "three":"3", "four":"4",
          "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    temp_word = ""
    answer = ""
    for i in s:
        if i in dic.values():
            answer = answer + i
        else:
            temp_word = temp_word + i
        if temp_word in dic.keys():
            answer = answer + str(dic.get(temp_word))
            temp_word = ""
    return int(answer)