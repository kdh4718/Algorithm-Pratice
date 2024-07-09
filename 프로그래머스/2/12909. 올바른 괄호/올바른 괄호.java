import java.util.*;

class Solution {
    boolean solution(String s) {
        int answer = 0;

        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '('){
                answer += 1;
            }else{
                answer -= 1;
            }
            
            if (answer < 0){break;}
        }
    
        if (answer == 0){
            return true;
        }else {
            return false;
        }
    }
}