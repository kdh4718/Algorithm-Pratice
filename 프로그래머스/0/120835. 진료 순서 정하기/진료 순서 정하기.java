import java.util.*;

class Solution {
    public int[] solution(int[] emergency) {
        int n = emergency.length;
        int[] answer = new int[n];
        Integer[] order = new Integer[n];
        
        for (int i = 0; i < n; i++){
            order[i] = i;
        }
        
        Arrays.sort(order, (a, b) -> emergency[b] - emergency[a]);
        
        for (int i = 0; i < n; i++){
            answer[order[i]] = i + 1;
        }
        
        return answer;
    }
}