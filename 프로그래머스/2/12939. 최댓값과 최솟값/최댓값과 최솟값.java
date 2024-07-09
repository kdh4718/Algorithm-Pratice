import java.util.*;

class Solution {
    public String solution(String s) {
        int[] numberList = Arrays.stream(s.split(" "))
            .mapToInt(Integer::parseInt).toArray();
        int minNum = Arrays.stream(numberList).min().orElse(0);
        int maxNum = Arrays.stream(numberList).max().orElse(0);
        
        return minNum + " " + maxNum;
    }
}