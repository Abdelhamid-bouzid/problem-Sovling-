class Solution:
    def convertToTitle(self, n: int) -> str:
        
        s = ''
        i = 0
        while n>0:
            
            rem = n%26
            if rem==0:
                s = "Z"+s
                n = n//26 -1
            else:
                s = chr((rem-1)+ord("A"))+s
                n = n//26
                
            i +=1
                
        return s
