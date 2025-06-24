class Solution {
    static int sum(int n){
        int num = 0;
        
        if (n % 2 == 1){
            for (int i = 1; i <= n; i+=2){
                num += i;
            }
        }else{
            for (int i = 2; i <= n; i+=2){
                num += Math.pow(i, 2);
            }
        }
        
        return num;
    }
    
    public int solution(int n) {
        int answer = sum(n);
        return answer;
    }
}