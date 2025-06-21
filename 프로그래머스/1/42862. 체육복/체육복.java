import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;
        HashSet<Integer> hs = new HashSet<>();
        Arrays.sort(lost);
        
        for (int i : reserve){
            hs.add(i);
        }
        
        for (int i = 0; i < lost.length; i++){
            if (hs.contains(lost[i])){
                answer += 1;
                hs.remove(lost[i]);
                lost[i] = 0;
            }
        }
        
        for (int i : lost){
            if (i != 0){
                if (hs.contains(i - 1)){
                    answer += 1;
                    hs.remove(i - 1);
                }else if (hs.contains(i + 1)){
                    answer += 1;
                    hs.remove(i + 1);
                }
            }
        }
        
        return answer;
    }
}