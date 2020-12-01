class Solution:
    def isValid(self, s: str):
        
        p = ['()','{}','[]']
        l = []
        for i,el in enumerate(s):
            if len(l)>0 and (l[-1]+el in p):
                l.pop()
            else:
                l.append(el)
        if len(l)==0:
            return True
        else:
            return False
