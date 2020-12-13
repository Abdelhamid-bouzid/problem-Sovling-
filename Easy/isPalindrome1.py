class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = filter(str.isalnum, s)
        s = "".join(s).lower()

        if s==s[::-1]:
            return True
        else:
            return False
