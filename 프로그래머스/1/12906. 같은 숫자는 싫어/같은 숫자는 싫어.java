import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> tempList = new ArrayList<>();

        for (int a : arr) {
            if (tempList.size() == 0 || tempList.get(tempList.size() - 1) != a)             {
                tempList.add(a);
            }
        }

        int[] answer = new int[tempList.size()];
        for (int i = 0; i < tempList.size(); i++) {
            answer[i] = tempList.get(i);
        }
        
        return answer;
    }
}