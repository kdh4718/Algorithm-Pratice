import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        List<Integer> number = new ArrayList<>();
        
        for (int i = 0; i < my_string.length(); i++){
            if (Character.isDigit(my_string.charAt(i))){
                number.add((int)my_string.charAt(i));
            }
        }
        
        int[] answer = new int[number.size()];
        
        for (int i = 0; i < number.size(); i++){
            answer[i] = number.get(i) - 48;
        }
        Arrays.sort(answer);
        return answer;
    }
}