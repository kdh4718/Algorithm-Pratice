class Solution {
    public String solution(String s, int n) {
        String answer = "";
        
        for (int i = 0; i < s.length(); i++){
            char temp = s.charAt(i);
            if (Character.isUpperCase(temp)){
                answer += (char) ((temp + n - 'A')%26 + 'A');
            }else if (Character.isLowerCase(temp)){
                answer += (char) ((temp + n - 'a')%26 + 'a');
            }else{
                answer += temp;
            }
        }
        
        return answer;
    }
}