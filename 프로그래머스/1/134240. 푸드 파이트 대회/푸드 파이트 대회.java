class Solution {
    public String solution(int[] food) {
        String answer = "0";
        
        for (int i = food.length-1; i > 0; i--){
            String f = Integer.toString(i).repeat((int) Math.floor(food[i]/2));
            answer = f + answer + f;
        }
        
        return answer;
    }
}