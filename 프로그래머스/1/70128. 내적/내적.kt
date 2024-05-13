class Solution {
    fun solution(a: IntArray, b: IntArray): Int {
        var answer: Int = a.zip(b) { i, j, -> i*j}.sum()
        return answer
    }
}