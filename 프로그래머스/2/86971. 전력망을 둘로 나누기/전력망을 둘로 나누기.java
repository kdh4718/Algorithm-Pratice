import java.util.*;

class Solution {
    static int[][] maps;
    
    static int bfs(int n){
        boolean[] visited = new boolean[maps.length];
        int count = 0;
        Deque<Integer> queue = new ArrayDeque<>();
        
        visited[n] = true;
        queue.offerLast(n);
        
        while (!queue.isEmpty()){
            int cur = queue.pollFirst();
            
            for (int i = 0; i < maps.length; i++){
                if (maps[cur][i] == 1 && !visited[i]){
                    count += 1;
                    visited[i] = true;
                    queue.offerLast(i);
                }
            }
        }
        
        return count;
    }
    
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        maps = new int[n + 1][n + 1];
        
        for (int[] wire : wires){
            maps[wire[0]][wire[1]] = 1;
            maps[wire[1]][wire[0]] = 1;
        }
        
        for (int[] wire : wires){
            maps[wire[0]][wire[1]] = 0;
            maps[wire[1]][wire[0]] = 0;
            
            int wireA = bfs(wire[0]);
            int wireB = bfs(wire[1]);
            
            answer = Math.min(answer, Math.abs(wireA - wireB));
            
            maps[wire[0]][wire[1]] = 1;
            maps[wire[1]][wire[0]] = 1;
        }
        
        return answer;
    }
}