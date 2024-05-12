class Solution {
    fun solution(numbers: IntArray): Int {
        val answer: IntArray = intArrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9)
        var sum: Int = 0
        
        for (i in answer){
            if (i !in numbers){
                sum += i
            }
        }
        
        return sum
    }
}