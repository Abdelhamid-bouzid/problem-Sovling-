class Solution:
    def addBinary(self, a: str, b: str):
        n = int(a,2) + int(b,2)
        s = str(bin(n))[2:]
        return s
