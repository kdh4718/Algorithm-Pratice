class Solution {
    public long solution(long n) {
        int intnum = (int) Math.sqrt(n);
        if (Math.pow((int) Math.sqrt(n), 2) == n){
            return (long)Math.pow((int) Math.sqrt(n)+1, 2);
        }

        return -1;
    }
}