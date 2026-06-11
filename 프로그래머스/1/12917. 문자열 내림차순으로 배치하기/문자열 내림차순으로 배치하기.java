import java.util.Arrays;

class Solution {
    public String solution(String s) {
        char[] divide = s.toCharArray();
        Arrays.sort(divide);
        
        String answer = new StringBuilder(new String(divide)).reverse().toString();
        
        return answer;
    }
}