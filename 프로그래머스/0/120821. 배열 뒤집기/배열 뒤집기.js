function solution(num_list) {
    let answer = [];
    for (i=num_list.length-1;i>-1;i--) {
        answer.push(num_list[i])
    }
    return answer;
}
