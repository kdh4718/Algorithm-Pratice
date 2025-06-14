class Solution {
    static boolean[] visited;
    
    public void dfs(int x, int[][] computers){
        visited[x] = true;
        
        for (int i = 0; i < computers[0].length; i++){
            if (computers[x][i] == 1 && !visited[i]){
                dfs(i, computers);
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        visited = new boolean[n];
        int answer = 0;
        
        for (int i = 0; i < n; i++){
            if (!visited[i]){
                answer += 1;
                dfs(i, computers);
            }
        }
        
        return answer;
    }
}