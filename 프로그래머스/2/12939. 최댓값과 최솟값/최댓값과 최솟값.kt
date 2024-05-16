class Solution {
    fun solution(s: String): String {
        var answer = s.split(" ").map { it.toInt()}.toIntArray()

        return answer.minOrNull().toString() + " " + answer.maxOrNull().toString()
    }
}