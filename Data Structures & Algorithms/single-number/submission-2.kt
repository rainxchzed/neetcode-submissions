class Solution {
    fun singleNumber(nums: IntArray): Int {
        nums.sort()
        var s: Int? = nums[0]
        var lastSaved = nums[0]

        for(i in 1 .. nums.size - 1) {
            if(s == nums[i]) {
                s = null
            }

            if(s == null) {
                if(nums[i] != lastSaved) {
                    s = nums[i]

                    lastSaved = nums[i]
                }
            }
        }

        return s ?: lastSaved
    }

    // [-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]
    // 

    // [7,6,6,7,8]
}
