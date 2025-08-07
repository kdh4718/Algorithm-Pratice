import java.util.*;

class Solution {
    public String solution(String my_string) {
        String answer = my_string.toLowerCase();
        
        char[] ch = answer.toCharArray();
        Arrays.sort(ch);
        
        return new String (ch);
    }
}