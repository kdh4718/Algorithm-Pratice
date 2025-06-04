class Solution {
    int answer = 0;
    public void dfs(int[] numbers, int target, int loc, int sumNumber){
        if (loc == numbers.length){
            if (sumNumber == target){
                answer += 1;
            }
            return;
        }
        
        dfs(numbers, target, loc + 1, sumNumber + numbers[loc]);
        dfs(numbers, target, loc + 1, sumNumber - numbers[loc]);
    }
    
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        return answer;
    }
}