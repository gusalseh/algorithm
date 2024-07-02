function solution(a, b) {
    let answer = 0;
    let s1 = 0;
    let s2 = 0;
    s1 = a.toString() + b.toString()
    s2 = 2 * a * b
    if (s1 > s2) {
        answer = parseInt(s1)
    } else {
        answer = s2
    }
    return answer;
}