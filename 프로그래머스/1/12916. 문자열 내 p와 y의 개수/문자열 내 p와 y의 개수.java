class Solution {
    boolean solution(String s) {
        boolean answer = true;
        String low = s.toLowerCase();
        
        int cnt = 0;
        
        for (int i = 0; i < low.length(); i++){
            char c = low.charAt(i);
            if (c == 'p'){
                cnt++;
            }else if (c == 'y'){
                cnt--;
            }
        }

        return cnt==0;
    }
}