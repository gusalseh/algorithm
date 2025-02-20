class Solution {
    public int[] solution(int[] arr) {
        int temp=arr[0];
        if (arr.length==1) {
            return new int[] {-1};
        }
        for(int i: arr) {
            if (i<temp) {
                temp = i;
            }
        }
        int[] answer = new int[arr.length-1];
        int idx = 0;
        for(int j: arr) {
            if (j!=temp) {
                answer[idx++]=j;
            }
        }
        return answer;
    }
}