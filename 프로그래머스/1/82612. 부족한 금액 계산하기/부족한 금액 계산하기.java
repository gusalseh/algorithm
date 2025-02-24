class Solution {
    public long solution(int price, int money, int count) {
        long answer = money;
        long total_price = 0;
        for(int i=1;i<=count;i++) {
            total_price+=i*price;
        }
        answer = total_price - money;
        if (answer<=0) {
            return 0;
        } else {
            return answer;
        }
    }
}