class Solution {
    static int answer = 0;
    
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        
        trip(dungeons, visited, 0, k);
        
        return answer;
    }
    
    static void trip(int[][] dungeons, boolean[] visited, int count, int k){
        answer = Math.max(answer, count);
        
        for (int i = 0; i < dungeons.length; i++){
            if (!visited[i]){
                if (k >= dungeons[i][0]){
                    visited[i] = true;
                    trip(dungeons, visited, count + 1, k - dungeons[i][1]);
                    visited[i] = false;
                }
            }
        }
    }
}