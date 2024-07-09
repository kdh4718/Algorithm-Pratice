import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int minNum = Arrays.stream(arr).min().orElse(0);
        int[] answer = Arrays.stream(arr).filter(it -> it != minNum).toArray();
        
        if (answer.length == 0) {
            return new int[] {-1};
        }
        
        return answer;
    }
}