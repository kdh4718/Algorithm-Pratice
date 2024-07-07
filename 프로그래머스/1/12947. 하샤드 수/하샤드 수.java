class Solution {
    public boolean solution(int x) {
        int answer = 0;
        int a = x;
        while(a > 0){
            answer += a % 10;
            a /= 10;
        }
        return x%answer == 0;
    }
}