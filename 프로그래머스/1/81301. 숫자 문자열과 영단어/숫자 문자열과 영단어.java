class Solution {
    public int solution(String s) {
        String[] number = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        
        for (int i = 0 ; i < 10; i++){
            s = s.replace(number[i], String.valueOf(i));
        }
        
        return Integer.parseInt(s);
    }
}