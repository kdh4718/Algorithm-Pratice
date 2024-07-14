class Solution {
    public int solution(int n) {
        int answer = n+1;
        long startNum = Integer.bitCount(n);
        while (true){
            long bigNum = Integer.bitCount(answer);
            if (startNum == bigNum){
                break;
            }
            answer++;
        }
        
        return answer;
    }
}