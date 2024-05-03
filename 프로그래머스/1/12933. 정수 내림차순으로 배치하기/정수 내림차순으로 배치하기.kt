class Solution {
    fun solution(n: Long): Long {
        var answer = n.toString().toCharArray()
        
        return String(answer.sortedArrayDescending()).toLong()
    }
}