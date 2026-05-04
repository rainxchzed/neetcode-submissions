class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        appearances = {}
        for num in nums:
            if num not in appearances:
                appearances[num] = 1
            else:
                appearances[num] = appearances[num] + 1
        print(appearances)

        for key_num, value_count in appearances.items():
            if value_count > 1:
                for i in range(1, value_count):
                    nums.remove(key_num)

        return len(nums)


