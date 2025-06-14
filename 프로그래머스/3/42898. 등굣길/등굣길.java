class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] answer = new int[m + 1][n + 1];
        answer[1][1] = 1;
        
        for (int[] pud: puddles){
            answer[pud[0]][pud[1]] = -1;
        }
        
        for (int i = 1; i <= m; i++){
            for (int j = 1; j <= n; j++){
                if (i == 1 && j == 1){ continue; }
                if (answer[i][j] == -1){ 
                    answer[i][j] = 0;
                    continue;
                }
                
                answer[i][j] = (answer[i - 1][j] + answer[i][j - 1])%1000000007;
            }
        }
        
        return answer[m][n];
    }
}