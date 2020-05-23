class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        # check if the substring is in the string
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1