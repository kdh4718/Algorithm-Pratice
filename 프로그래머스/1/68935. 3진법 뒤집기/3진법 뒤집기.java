class Solution {
    public int solution(int n) {
        StringBuffer answer = new StringBuffer(Integer.toString(n, 3));
        String result = answer.reverse().toString();
        return Integer.parseInt(result, 3);
    }
}