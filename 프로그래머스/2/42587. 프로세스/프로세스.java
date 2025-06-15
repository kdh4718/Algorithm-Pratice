import java.util.*;

class Solution {
    static class Process {
        int priority;
        int index;

        Process(int priority, int index) {
            this.priority = priority;
            this.index = index;
        }
    }

    public int solution(int[] priorities, int location) {
        Queue<Process> queue = new LinkedList<>();
        int[] priorityCount = new int[10]; 

        for (int i = 0; i < priorities.length; i++) {
            int p = priorities[i];
            queue.offer(new Process(p, i));
            priorityCount[p]++;
        }

        int answer = 0;
        int currentMax = 9;

        while (!queue.isEmpty()) {
            Process current = queue.poll();

            while (priorityCount[currentMax] == 0) {
                currentMax--;
            }

            if (current.priority == currentMax) {
                answer++;
                priorityCount[currentMax]--;

                if (current.index == location) {
                    return answer;
                }
            } else {
                queue.offer(current); 
            }
        }

        return answer;
    }
}
