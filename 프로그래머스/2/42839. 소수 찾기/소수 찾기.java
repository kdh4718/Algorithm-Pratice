import java.util.*;

class Solution {
    static Set<Integer> numSet = new HashSet<>();
    
    public int solution(String numbers) {
        boolean[] visited = new boolean[numbers.length()];
        int answer = 0;
        
        makeNum("", numbers, visited);
        
        for (int num : numSet){
            if (isPrime(num)){
                answer += 1;
            }
        }
        
        return answer;
    }
    
    static void makeNum(String cur, String numbers, boolean[] visited){
        if (!cur.equals("")){
            numSet.add(Integer.parseInt(cur));
        }
        
        for (int i = 0; i < numbers.length(); i++){
            if (!visited[i]){
                visited[i] = true;
                makeNum(cur + numbers.charAt(i), numbers, visited);
                visited[i] = false;
            }
        }
    }
    
    static boolean isPrime(int num){
        if (num < 2){
            return false;
        }
        
        for (int i = 2; i <= Math.sqrt(num); i++){
            if (num % i == 0){
                return false;
            }
        }
        
        return true;
    }
}