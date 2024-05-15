class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        val payment = (1..count).sumOf { it * price.toLong() }
        val shortage = if (payment > money) payment - money else 0
        
        return shortage
    }
}
