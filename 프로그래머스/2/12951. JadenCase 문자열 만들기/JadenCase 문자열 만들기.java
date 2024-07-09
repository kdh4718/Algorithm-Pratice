class Solution {
    public String solution(String s) {
        String answer = "";
        boolean flag = true;

        for (int i = 0; i < s.length(); i++){
            char currentChar = s.charAt(i);
            if (!flag){
                answer += Character.toLowerCase(currentChar);
            }else{
                answer += Character.toUpperCase(currentChar);
            }
            flag = (currentChar == ' ');
        }
        
        return answer;
    }
}