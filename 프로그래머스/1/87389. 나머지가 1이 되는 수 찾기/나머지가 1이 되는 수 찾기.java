class Solution {
    public int solution(int n) {
        int target_num = n-1;
        int answer = 0;
        int count = 0;
        for (int i = 1;i<=target_num;i++) {
            if(target_num%i==0) {
                count += 1;
                if(count==2) {
                    answer = i;
                }
            }
        }
        return answer;
    }
}