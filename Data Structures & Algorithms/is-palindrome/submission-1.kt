class Solution {
    fun isPalindrome(s: String): Boolean {
        val s = s.filter { it.isLetterOrDigit() }.lowercase()

        return s == s.reversed()
    }
}
