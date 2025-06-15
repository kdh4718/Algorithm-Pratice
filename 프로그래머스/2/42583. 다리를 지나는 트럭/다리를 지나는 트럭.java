import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int location = 0;
        int totalWeight = 0;
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 0; i < bridge_length; i++){
            queue.offer(0);
        }
        
        while (location < truck_weights.length){
            totalWeight -= queue.poll();
            
            if (totalWeight + truck_weights[location] <= weight){
                queue.offer(truck_weights[location]);
                totalWeight += truck_weights[location];
                location += 1;
            }else{
                queue.offer(0);
            }
            answer += 1;
        }
        
        answer += bridge_length;
        
        return answer;
    }
}