class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        
        l= [[1]]
        for i in range(1,numRows):
            
            l1 = [1]
            for j in range(1,i):
                l1.append(l[-1][j-1]+l[-1][j])
            l1.append(1)
            
            l.append(l1)
                
        return l
