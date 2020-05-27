# Runtime Complexity: O(n) due to iterating over all the characters in the string
# Space Complexity: O(n) due the dictionary created by collections.counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequent_map = collections.Counter(s)
        
        for g in enumerate(s):
            idx, value = g
            if frequent_map[value] == 1:
                return idx
        return -1
        
        