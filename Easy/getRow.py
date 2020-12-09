class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        i = 1
        l = [[1]]
        while i<rowIndex+1:
            
            row = [1]
            for j in range(1,i):
                row.append(l[-1][j-1]+l[-1][j])
            row.append(1)
            l.append(row)
            i+=1
        return row
        
