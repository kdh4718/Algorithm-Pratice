class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        
        while (!s.equals("1")){
            int sizeBefore = s.length();
            s = s.replace("0", "");
            int sizeAfter = s.length();
            
            s = Integer.toBinaryString(sizeAfter);
            
            answer[1] += sizeBefore - sizeAfter;
            answer[0] += 1;
        }
        
        return answer;
    }
}