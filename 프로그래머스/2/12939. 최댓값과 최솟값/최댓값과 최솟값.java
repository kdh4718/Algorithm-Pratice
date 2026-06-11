import java.util.*;

class Solution {
    public String solution(String s) {
        int[] number = Arrays.stream(s.split(" "))
            .mapToInt(Integer::parseInt).toArray();
        int min = Arrays.stream(number).min().orElse(0);
        int max = Arrays.stream(number).max().orElse(0);
        
        return min + " " + max;
    }
}