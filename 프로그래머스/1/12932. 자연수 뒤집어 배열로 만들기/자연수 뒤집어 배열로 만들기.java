class Solution {
    public int[] solution(long n) {
        String a = "" + n;
        int[] answer = new int[a.length()];
        int loc = 0;
        
        while (n > 0){
            answer[loc] = (int) (n % 10);
            n /= 10;
            loc += 1;
        }
        
        return answer;
    }
}