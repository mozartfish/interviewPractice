class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = collections.Counter(s)
        
        for idx, char in enumerate(s):
            if hmap[char] == 1:
                return idx
        
        return -1
        