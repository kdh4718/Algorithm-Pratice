import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int sco : scoville){
            pq.add(sco);
        }
        
        while (pq.size() >= 2){    
            if (pq.peek() >= K){
                return answer;
            }else{
                int first = pq.poll();
                int second = pq.poll();
                answer += 1;
                pq.add(first + (second * 2));
            }
        }
        
        
        
        return pq.peek() >= K ? answer : -1;
    }
}