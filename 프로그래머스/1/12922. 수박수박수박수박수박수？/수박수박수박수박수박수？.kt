class Solution {
    fun solution(n: Int): String {
        var answer = "수박".repeat(n/2) + "수".repeat(n%2)
        return answer
    }
}