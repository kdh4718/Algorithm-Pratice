class Solution {
    public boolean solution(int x) {
        int answer = String.valueOf(x).chars().map(i -> i - '0').sum();
        return x%answer == 0;
    }
}