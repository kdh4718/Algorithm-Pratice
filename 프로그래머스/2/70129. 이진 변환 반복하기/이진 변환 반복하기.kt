class Solution {
    fun solution(s: String): IntArray {
        var change: Int = 0
        var count: Int = 0
        var string: String = s
        
        while (string != "1"){
            change += 1
            count += string.replace("1", "").count()
            string = Integer.toBinaryString(string.replace("0", "").count())
        }
        
        return intArrayOf(change, count)
    }
}