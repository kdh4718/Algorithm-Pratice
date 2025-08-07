import java.util.*;

class Solution {
    public String solution(int age) {
        String answer = "";
        String ageStr = Integer.toString(age);
        Map<Integer, Character> map = new HashMap<>();
        
        for (int i = 0; i < 10; i++){
            char c = (char) ('a' + i);
            map.put(i, c);
        }
        
        for (int i = 0; i < ageStr.length(); i++){
            int n = (int) (ageStr.charAt(i) - '0');
            answer += map.get(n);
        }
        
        return answer;
    }
}