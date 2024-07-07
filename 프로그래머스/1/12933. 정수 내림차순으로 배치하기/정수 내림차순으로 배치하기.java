import java.util.*;

class Solution {
    public long solution(long n) {
        String[] answer = String.valueOf(n).split("");
        Arrays.sort(answer);
        
        StringBuilder sb = new StringBuilder();
        for (String i : answer) sb.append(i);
        
        return Long.parseLong(sb.reverse().toString());
    }
}