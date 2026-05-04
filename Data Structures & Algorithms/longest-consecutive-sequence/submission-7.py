class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0

        srtd = sorted(nums)
        longest = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        last = srtd[0]
        curr = 0
        print(srtd)

        for n in srtd:
            if n == last + 1:
                longest[curr] = longest[curr] + 1
            elif n == last:
                continue
            else:
                curr += 1
            last = n
            
                        
        return max(longest)


