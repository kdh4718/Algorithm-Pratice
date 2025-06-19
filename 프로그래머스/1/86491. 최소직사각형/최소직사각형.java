class Solution {
    public int solution(int[][] sizes) {
        int answer;
        int row = 0;
        int col = 0;
        
        for (int[] size : sizes){
            row = Math.max(row, Math.min(size[0], size[1]));
            col = Math.max(col, Math.max(size[0], size[1]));
        }
        answer = row * col;
        
        return answer;
    }
}