import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hm = new HashMap<>();
        
        for (String[] clo : clothes){
            hm.put(clo[1], hm.getOrDefault(clo[1], 1) + 1);
        }
        
        for (String key : hm.keySet()){
            answer *= hm.get(key);
        }
        
        return answer - 1;
    }
}