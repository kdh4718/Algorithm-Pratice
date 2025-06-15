import java.util.*;

class Solution {
    static class Process{
        int priority, index;
        
        Process(int priority, int index){
            this.priority = priority;
            this.index = index;
        }
    }
    
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int topPriority = 9;
        int[] countPriority = new int[10];
        Queue<Process> queue = new LinkedList<>();
        
        for (int i = 0; i < priorities.length; i++){
            int num = priorities[i];
            
            queue.offer(new Process(num, i));
            countPriority[num] += 1;
        }
        
        while (!queue.isEmpty()){
            Process cur = queue.poll();
            
            while (countPriority[topPriority] == 0){
                topPriority -= 1;
            }
            
            if (cur.priority == topPriority){
                answer += 1;
                countPriority[topPriority] -= 1;
                
                if (cur.index == location){
                    return answer;
                }
                continue;
            }
            queue.offer(cur);
        }
        
        return answer;
    }
}