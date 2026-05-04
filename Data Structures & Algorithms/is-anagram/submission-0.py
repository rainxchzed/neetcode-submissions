class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sL = list(s)

        for char in t:
            try:
                sL.remove(char)
            except ValueError:
                pass
        
        if len(sL) <= 0:
            return True
        else:
            return False