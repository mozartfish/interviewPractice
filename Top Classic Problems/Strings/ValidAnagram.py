class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the words
        s = sorted(s)
        t = sorted(t)
        
        return s == t