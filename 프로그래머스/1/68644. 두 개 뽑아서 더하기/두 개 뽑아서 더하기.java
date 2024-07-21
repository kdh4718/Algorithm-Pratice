import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> answer = new TreeSet<>();
        
        for (int i = 0; i < numbers.length; i++){
            for (int j = i + 1; j < numbers.length; j++){
                answer.add(numbers[i] + numbers[j]);
            }
        }
        
        int[] result = new int[answer.size()];
         int i = 0;

        for (Integer num : answer) {
            result[i++] = num;
        }
        
        return result;
    }
}