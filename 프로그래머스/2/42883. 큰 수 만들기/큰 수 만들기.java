import java.util.*;

class Solution {
    public String solution(String number, int k) {
        char[] answer = new char[number.length() - k];
        Deque<Integer> queue = new ArrayDeque<>();
        
        for (int i = 0; i < number.length(); i++) {
            int digit = number.charAt(i) - '0';

            while (!queue.isEmpty() && k > 0 && queue.peekLast() < digit) {
                queue.pollLast();
                k--;
            }

            queue.offerLast(digit);
        }
        
        while (k > 0){
            k -= 1;
            queue.pollLast();
        }
        
        for (int i = 0; i < answer.length; i++){
            answer[i] = (char) (queue.pollFirst() + '0');
        }
        
        return new String(answer);
    }
}