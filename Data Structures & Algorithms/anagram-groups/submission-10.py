class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        while strs:
            target = strs[0]
            currList = [target]
            print(f"Starting new iteration with: {strs}")
            strs.remove(target)

            i = 0
            
            while i < len(strs):
                print(f"Are {target} and {strs[i]} anagrams?")
                if self.areAnagrams(target, strs[i]):
                    currList.append(strs[i])
                    strs.remove(strs[i])

                else:
                    i += 1

            res.append(currList)
        
        return res
    
    def areAnagrams(self, str1, str2):
        return sorted(str1) == sorted(str2)

