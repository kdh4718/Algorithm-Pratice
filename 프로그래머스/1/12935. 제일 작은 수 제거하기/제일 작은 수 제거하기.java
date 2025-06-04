import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        
        if (arr.length == 1){
            return new int[] {-1};
        }
        
        int minNumber = Arrays.stream(arr).min().getAsInt();
        answer = Arrays.stream(arr).filter(i -> i != minNumber).toArray();
            
        return answer;
    }
}