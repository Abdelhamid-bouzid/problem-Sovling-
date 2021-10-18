class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        
        cache = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        result = 0
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, self.helper(matrix, i, j, cache))
                
        return result
        
    def helper(self, matrix, i, j, cache):
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        if cache[i][j] != 0:
            return cache[i][j]
        
        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]
            
            if 0 <= x and x < len(matrix) and 0 <= y and y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                cache[i][j] = max(cache[i][j], self.helper(matrix, x, y, cache))
        
        cache[i][j] += 1
        
        return cache[i][j]
        
