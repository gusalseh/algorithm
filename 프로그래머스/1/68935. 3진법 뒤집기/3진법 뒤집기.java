// import java.io.*;

// class Solution {
//     public int solution(int n) {
//         int answer = 0;
//         int mok = n;
//         int namoji = 0;
//         String target_num = "";
//         int count = 0;
//         while(true) {
//             namoji=mok%3;
//             mok/=3;
//             if (mok==1) {
//                 target_num+=namoji;
//                 target_num+=mok;
//                 count += 2;
//                 break;
//             } else {
//                 target_num += namoji;
//                 count += 1;
//             }
//         }
//         System.out.println(target_num);
//         for(int i=0;i<count;i++) {
//             int temp = (int) Math.pow(3,count-i-1);
//             if(target_num.charAt(i)!=0) {
//                 answer += (target_num.charAt(i)-'0')*temp;
//             }
//         }
        
//         return answer;
//     }
// }

class Solution {
    public int solution(int n) {
        int answer = 0;
        int mok = n;
        int namoji;
        StringBuilder targetNum = new StringBuilder();
        
        while (mok > 0) {
            namoji = mok % 3;
            mok /= 3;
            targetNum.append(namoji);
        }
        
        String reversedTarget = targetNum.toString();
        
        int length = reversedTarget.length();
        for (int i = 0; i < length; i++) {
            int temp = (int) Math.pow(3, length - i - 1);
            answer += (reversedTarget.charAt(i) - '0') * temp;
        }
        
        return answer;
    }
}