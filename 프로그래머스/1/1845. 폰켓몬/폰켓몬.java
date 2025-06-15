import java.util.*;

class Solution {
    public int solution(int[] nums) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        int answer = nums.length / 2;
        
        for (int num : nums){
            hm.put(num, hm.getOrDefault(num, 0) + 1);
        }
        
        return Math.min(answer, hm.size());
    }
}