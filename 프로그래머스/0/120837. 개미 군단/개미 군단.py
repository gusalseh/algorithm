def solution(hp):
    answer = 0
    ant_1 = hp//5
    hp = hp - ant_1*5
    ant_2 = hp//3
    hp = hp - ant_2*3
    ant_3 = hp
    answer = ant_1 + ant_2 + ant_3
    return answer