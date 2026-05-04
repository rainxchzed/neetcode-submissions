class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        apr = {}
        res = 0

        for i in range(len(nums)):
            if nums[i] in apr:
                apr[nums[i]] = apr[nums[i]] + 1
                if apr[nums[i]] > (len(nums) / 2):
                    res = nums[i]
            else:
                apr[nums[i]] = 1

        return res