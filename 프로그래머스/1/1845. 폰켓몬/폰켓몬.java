import java.util.*;

class Solution {
    public int solution(int[] nums) {
        HashSet<Integer> numSet = new HashSet<Integer>();
        
        for (int num : nums){
            numSet.add(num);
        }
        
        int answer = Math.min(nums.length/2, numSet.size());
        return answer;
    }
}