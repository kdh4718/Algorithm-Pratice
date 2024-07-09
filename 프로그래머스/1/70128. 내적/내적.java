import java.util.stream.*;

class Solution {
    public int solution(int[] a, int[] b) {
        int answer = IntStream.range(0, a.length).map(i -> a[i]*b[i]).sum();
        return answer;
    }
}