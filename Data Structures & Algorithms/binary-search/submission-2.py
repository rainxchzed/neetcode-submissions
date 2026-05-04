class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while R >= L:
            m = (L + R) // 2

            if nums[m] > target:
                R = m - 1
            elif nums[m] < target:
                L = m + 1
            else:
                return m

        return -1