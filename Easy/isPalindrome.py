class Solution:
    def isPalindrome(self, x: int):
        if abs(x)>(2**31 -1):
            return False
        else:
            if str(x)==str(x)[::-1]:
                return True
            else:
                return False
