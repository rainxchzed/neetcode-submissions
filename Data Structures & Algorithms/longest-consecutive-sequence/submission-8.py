class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0

        srtd = sorted(nums)
        currentStreak = 1
        bestStreak = 1
        last = srtd[0]
        curr = 0
        print(srtd)

        for n in srtd:
            if n == last + 1:
                currentStreak +=1
                if currentStreak > bestStreak:
                    bestStreak = currentStreak
            elif n == last:
                continue
            else:
                
                currentStreak = 1
            last = n
            
                        
        return bestStreak


