import java.util.Collections;
import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int limit = budget;
        Arrays.sort(d);
        for(int i: d) {
            if(limit-i>=0) {
                limit-=i;
                answer+=1;
            } else {
                break;
            }
        }
        return answer;
    }
}