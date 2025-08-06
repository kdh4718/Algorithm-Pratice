class Solution {
    static boolean cross(int[] stones, int k, int p){
        int jump = 0;
        
        for (int stone : stones){
            if (stone - p < 0){
                jump += 1;
                
                if (jump >= k){
                    return false;
                }
            }else{
                jump = 0;
            }
        }
        
        return true;
    }
    
    public int solution(int[] stones, int k) {
        int answer = 0;
        int left = 0;
        int right = Integer.MAX_VALUE;
        
        while (left <= right){
            int mid = (left + right) / 2;
            
            if (cross(stones, k, mid)){
                answer = mid;
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        
        return answer;
    }
}