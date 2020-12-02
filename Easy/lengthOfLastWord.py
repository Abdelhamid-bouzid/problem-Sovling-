class Solution:
    def lengthOfLastWord(self, s: str):
        w = s.split()
        if len(w)==0:
            return 0
        else:
            return len(w[-1])
