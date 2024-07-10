class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int pLen = p.length();
        long small = Long.parseLong(p);
        
        for (int i = 0; i <= t.length() - pLen; i++){
            long big = Long.parseLong(t.substring(i, i + pLen));

            if (big <= small) answer += 1;
        }

        return answer;
    }
}