class Solution:
    def strStr(self, haystack: str, needle: str):
        if needle:
            index = haystack.find(needle)
            return index
        else:
            return 0
