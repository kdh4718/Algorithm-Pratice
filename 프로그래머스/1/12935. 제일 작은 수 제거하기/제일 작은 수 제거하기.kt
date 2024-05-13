class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer = arr.filter { it != arr.minOrNull()}.toIntArray()
        return if (answer.isEmpty()) intArrayOf(-1) else answer
    }
}