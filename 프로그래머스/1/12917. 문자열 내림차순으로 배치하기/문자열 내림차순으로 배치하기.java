import java.util.Arrays;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        Character[] charArray = new Character[s.length()];
        for (int i = 0; i < s.length(); i++) {
            charArray[i] = s.charAt(i);
        }

        Arrays.sort(charArray, Collections.reverseOrder());

        StringBuilder sb = new StringBuilder();
        for (char c : charArray) {
            sb.append(c);
        }

        return sb.toString();
    }
}