'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        l,r = 0,len(matrix[0])-1
        top,down = 0,len(matrix)-1
        
        i = 0
        while top<=down and l<=r:
            row = i%2
            if row==0:
                res.extend(matrix[top][l:r+1])
                top +=1
                for j in range(top,down+1):
                    res.append(matrix[j][r])
                r -=1
                
            else:
                res.extend(matrix[down][l:r+1][::-1])
                down -=1
                for j in reversed(range(top,down+1)):
                    res.append(matrix[j][l])
                l +=1
                
            i +=1
                
        return res
                    


            
