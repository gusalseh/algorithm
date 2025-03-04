class Solution {
    public int solution(int[] number) {
        int answer = 0;
        int num_i = 0;
        int num_j = 0;
        for(int i=0;i<number.length-2;i++) {
            num_i=number[i];
            for(int j=i+1;j<number.length-1;j++) {
                for(int k=j+1;k<number.length;k++) {
                    if (number[i]+number[j]+number[k]==0) {
                        answer ++;
                    }
                }
            }
        }
        return answer;
    }
}