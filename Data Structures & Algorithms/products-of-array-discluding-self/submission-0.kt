class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
//         Input: nums = [1,2,4,6]

// Output: [48,24,12,8]
// 2 * 4 * 6 = 48
// 1 * 4 * 6 = 24
// 1 * 2 * 6 = 12
// 1 * 2 * 4 = 8

        val result = mutableListOf<Int>()
        for(i in 0 .. nums.size - 1) {
            var sum = 1

            for(j in 0 .. nums.size - 1) {
                if(j != i) {
                    sum *= nums[j]
                }
            }

            result.add(sum)
        }

        return result.toIntArray()
    }
}
