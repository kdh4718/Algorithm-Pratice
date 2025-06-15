import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer;
        List<Integer> stack = new ArrayList<>();
        int pre = -1;
        
        for (int num : arr){
            if (num != pre){
                stack.add(num);
            }
            pre = num;
        }
        
        answer = new int[stack.size()];
        
        for (int i = 0; i < stack.size(); i++){
            answer[i] = stack.get(i);
        }

        return answer;
    }
}