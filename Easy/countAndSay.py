class Solution:
    def countAndSay(self, n: int):
        if n==1:
            return "1"
        
        s1 = self.countAndSay(n-1)
        
        s = ''
        l = 1
        for i in range(1,len(s1)+1):
            if i < len(s1) and s1[i]==s1[i-1]:
                l+=1
            else:
                s =s+str(l)+s1[i-1]
                l = 1
            
        return s
