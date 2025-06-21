import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int first = 0, last = people.length - 1; 
        
        Arrays.sort(people);
        
        while (first <= last){
            if (first == last){
                answer += 1;
                break;
            }
            
            if (people[first] + people[last] <= limit){
                answer += 1;
                first += 1;
                last -= 1;
            }else{
                answer += 1;
                last -= 1;
            }
        }
        
        return answer;
    }
}