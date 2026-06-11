class Solution {
    public long solution(int price, int money, int count) {
        long total = (long) price * count * (count + 1) / 2;

        return Math.max(total - money, 0);
    }
}