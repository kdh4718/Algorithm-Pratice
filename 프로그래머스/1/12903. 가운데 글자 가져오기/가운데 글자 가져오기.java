class Solution {
    public String solution(String s) {
        String answer = "";
        int sLen = s.length();
        
        
        if (sLen % 2 == 1){
            answer = String.valueOf(s.charAt(sLen / 2));
        }else{
            answer = String.valueOf(s.charAt(sLen / 2 - 1)) + s.charAt(sLen / 2);
        }
        
        return answer;
    }
}