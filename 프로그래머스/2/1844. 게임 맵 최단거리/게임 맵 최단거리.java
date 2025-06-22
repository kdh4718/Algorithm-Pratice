import java.util.*;

class Solution {   
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    
    static class Location{
        int x, y, len;
        
        Location(int x, int y, int len){
            this.x = x;
            this.y = y;
            this.len = len;
        }
    }
    
    static int bfs(int[][] maps){
        Deque<Location> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        
        visited[0][0] = true;
        queue.offerLast(new Location(0, 0, 1));
        
        while (!queue.isEmpty()){
            Location cur = queue.pollFirst();
            
            if (cur.x == maps.length - 1 && cur.y == maps[0].length - 1){
                return cur.len;
            }
            
            for (int i = 0; i < 4; i++){
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                
                if (0 <= nx && nx < maps.length && 0 <= ny && ny < maps[0].length){
                    if (!visited[nx][ny] && maps[nx][ny] == 1){
                        visited[nx][ny] = true;
                        queue.offerLast(new Location(nx, ny, cur.len + 1));
                    }
                }
            }
        }
        
        return -1;
    }
    
    public int solution(int[][] maps) {
        int answer = bfs(maps);
        
        return answer;
    }
}