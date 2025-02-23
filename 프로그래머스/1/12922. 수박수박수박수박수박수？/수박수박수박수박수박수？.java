class Solution {
    public String solution(int n) {
        String answer = "";
        int num=n/2;
        if (n%2==0) {
            answer+=("수박").repeat(num);
        } else {
            answer+=("수박").repeat(num)+"수";
        }
        return answer;
    }
}