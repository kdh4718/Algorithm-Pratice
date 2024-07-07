import java.util.*;

class Solution {
    public long solution(long n) {
        String answer = Long.toString(n);
        ArrayList<Integer> arr = new ArrayList<>();
        
        for (int i = 0; i < answer.length(); i++){
            arr.add(answer.charAt(i) - '0');
        }
        
        arr.sort(Comparator.reverseOrder());
        
        StringBuilder sortedStr = new StringBuilder();
        for (int num : arr) {
            sortedStr.append(num);
        }
        
        return Long.parseLong(sortedStr.toString());
    }
}