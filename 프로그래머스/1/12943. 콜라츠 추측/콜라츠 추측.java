class Solution {
    public int solution(int num) {
        long real_num = num;
        int count = 0;
        while(real_num!=1) {
            if (real_num%2==0) {
                real_num/=2;
            } else {
                real_num=real_num*3+1;
            }
            count+=1;
        }
        if (count>=500) {
            return -1;
        }
        return count;
    }
}