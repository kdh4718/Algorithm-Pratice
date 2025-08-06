import java.util.*;

class Solution {
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int[][] map;
    
    static int[] progress(int x, int y, int dir, String[] board){  
        while (true){
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if (nx >= 0 && nx < map.length && ny >= 0 && ny < map[0].length){
                if (board[nx].charAt(ny) != 'D'){
                    x += dx[dir];
                    y += dy[dir];
                    
                    continue;
                }
            }
            break;
        }
        
        return new int[] {x, y};
    }
    
    public int solution(String[] board) {
        int answer = 0;
        map = new int[board.length][board[0].length()];
        Deque<int[]> deque = new ArrayDeque<>();
        
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length(); j++){
                if (board[i].charAt(j) == 'R'){
                    deque.offerLast(new int[] {i, j, 1});
                    break;
                }
            }
        }
        
        while (!deque.isEmpty()){
            int[] cur = deque.pollFirst();
            
            for (int i = 0; i < 4; i++){
                int[] loc = progress(cur[0], cur[1], i, board);
                
                if (board[loc[0]].charAt(loc[1]) == 'G'){
                    return cur[2];
                }
                
                if (map[loc[0]][loc[1]] == 0 || map[loc[0]][loc[1]] > cur[2]){
                    map[loc[0]][loc[1]] = cur[2];
                    
                    deque.offerLast(new int[] {loc[0], loc[1], cur[2] + 1});
                }
            }
        }
        
        return -1;
    }
}