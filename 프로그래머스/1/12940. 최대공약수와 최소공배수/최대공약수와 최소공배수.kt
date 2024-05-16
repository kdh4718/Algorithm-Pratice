class Solution {
    fun solution(n: Int, m: Int): IntArray {

        return intArrayOf(gcd(n, m), lcm(n, m))
    }
    tailrec fun gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
    fun lcm(a: Int, b: Int): Int = a*b/gcd(a, b)
}