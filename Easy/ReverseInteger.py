class Solution:
    def reverse(self, x: int):
        if x==0:
            return 0
        str1 = str(x)[::-1]
        str1 = str1.lstrip("0")
        
        if str1[-1]=='-':
            str1 = '-'+str1[:-1]
           
        if abs(int(str1)) > (2 ** 31 - 1):
            return 0
        else:
            return int(str1)
