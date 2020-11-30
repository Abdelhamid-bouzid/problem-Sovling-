class Solution:
    def romanToInt(self, s: str):
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        E = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM": 900}
        num  = 0
        for i,el in enumerate(s):
            if (i+1)<len(s) and s[i:i+2] in E:
                num += E[s[i:i+2]]
            elif (i)<len(s) and s[i-1:i+1] in E:
                num += 0
            else:
                num += d[el]
        return num
