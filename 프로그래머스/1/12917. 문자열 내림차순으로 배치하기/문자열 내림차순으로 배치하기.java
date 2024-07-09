import java.util.*;

class Solution {
    public String solution(String s) {
        String[] answer = s.split("");
        Arrays.sort(answer);
        
        StringBuilder result = new StringBuilder();
        for (String i : answer) {
            result.append(i);
        }
        
        return result.reverse().toString();
    }
}
