class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for(int i=left;i<=right;i++) {
            double result = Math.sqrt(i);
            if (result%1==0.0) {
                answer -= i;
            } else {
                answer += i;
            }
        }
        return answer;
    }
}