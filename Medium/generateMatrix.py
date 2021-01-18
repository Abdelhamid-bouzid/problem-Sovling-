'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
'''
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        visited = [[0] * n for _ in range(n)]
        matrix = [[0] * n for _ in range(n)]
        self.row, self.col = 0, 0
        self.curr = 1
        def spiral():
            move = False
            while self.col < n and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1
                self.col += 1
                move = True
            self.col -= 1
            self.row += 1
            while self.row < n and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1
                self.row += 1
                move = True
            self.row -= 1
            self.col -= 1
            while self.col >= 0  and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1
                self.col -= 1
                move = True
            self.col += 1
            self.row -= 1
            while self.row >= 0 and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1
                self.row -= 1
                move = True
            self.row += 1
            self.col += 1
            if move:
                spiral()
        spiral()
        return matrix
