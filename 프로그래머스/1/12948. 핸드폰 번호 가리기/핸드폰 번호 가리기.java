class Solution {
    public String solution(String phone_number) {
        int numSize = phone_number.length() -4;
        String answer = "*".repeat(numSize);
        
        answer += phone_number.substring(numSize);
        return answer;
    }
}