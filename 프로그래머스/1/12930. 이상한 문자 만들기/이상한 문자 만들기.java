class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arr = s.split("");
        int loc = 0;
        
        for (String i: arr){
            loc = (i.equals(" ")) ? 0 : loc + 1;
            i = (loc % 2 == 0) ? i.toLowerCase() : i.toUpperCase();
            answer += i;
        }
        
        return answer;
    }
}