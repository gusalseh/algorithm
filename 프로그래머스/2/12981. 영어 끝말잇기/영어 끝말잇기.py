def solution(n, words):
    archive = []
    out_person_num = 0
    out_num = 0

    for i in range(len(words)):
        if i == 0:
            archive.append(words[i])
            continue
        elif words[i] in archive:
            out_person_num = i%n + 1
            out_num = i//n + 1
            break
        elif words[i-1][-1] != words[i][0]:
            out_person_num = i%n + 1
            out_num = i//n + 1
            break
        elif len(words[i]) == 1:
            out_person_num = i%n + 1
            out_num = i//n + 1
            break
        else:
            archive.append(words[i])
    
    return [out_person_num, out_num]