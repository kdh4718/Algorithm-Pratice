import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer;
        Deque<Integer> deque = new ArrayDeque<>();
        List<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < progresses.length; i++){          
            int date = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
            
            if (!deque.isEmpty() && deque.peek() < date){
                list.add(deque.size());
                deque.clear();
            }
            deque.offer(date);
        }
        
        list.add(deque.size());
        answer = new int[list.size()];
            
        for (int i = 0; i < list.size(); i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}