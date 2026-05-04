class KthLargest(val k: Int, var nums: IntArray) {

    fun add(`val`: Int): Int {
        nums = nums + intArrayOf(`val`)

        println(nums.joinToString())
        
        nums.sort()

        println(nums.joinToString())

        return nums[nums.size - k]
    }

    // cool num: 3
    // initial input - [4, 5, 8, 2]
    // add - 3
    // add - 5
    // add - 10
    // add - 9
    // add - 4
    // expected - [4, 5, 5, 8, 8]

}
