class Solution {
    public int[] solution(int number1, int denom1, int number2, int denom2) {
        int num = number1 * denom2 + number2 * denom1;
        int den = denom1 * denom2;
        int div = 1;
        
        for (int i = 1; i <= num && i <= den; i++){
            if (num % i == 0 && den% i == 0){
                div = i;
            }
        }
        
        num /= div;
        den /= div;
        
        return new int[] {num, den};
    }
}