class Solution {
    public String solution(String s) {
        String answer = "";
        boolean flag = true;
        
        for (int i = 0; i < s.length(); i++){
            if (flag){
                answer += Character.toUpperCase(s.charAt(i));
            }else{
                answer += Character.toLowerCase(s.charAt(i));
            }
            
            flag = (s.charAt(i) == ' ');
        }
        
        return answer;
    }
}