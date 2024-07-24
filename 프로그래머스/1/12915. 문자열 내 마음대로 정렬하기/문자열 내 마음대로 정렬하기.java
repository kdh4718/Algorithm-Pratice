import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        int len = strings.length;
        String[] answer = new String[len];
        ArrayList<String> sort = new ArrayList<>();
        
        for (int i = 0; i < len; i++){
            sort.add(""+ strings[i].charAt(n) + strings[i]);
        }
        
        Collections.sort(sort);
        for (int i = 0; i < len; i++){
            answer[i] = sort.get(i).substring(1);
        }
        
        return answer;
    }
}