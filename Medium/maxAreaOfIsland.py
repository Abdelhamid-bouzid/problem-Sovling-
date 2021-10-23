class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid=grid
        self.n = len(grid)
        self.m = len(grid[0])
        self.vis = set()
        
        max_a = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j]==1 and (i,j) not in self.vis:
                    p = len(self.vis)
                    self.dfs(i,j)
                    max_a = max(max_a,len(self.vis)-p)
                    
        return max_a
        
        
    def dfs(self,i,j):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        self.vis.add((i,j))
        for dirc in directions:
            x = i+dirc[0]
            y = j+dirc[1]
            
            if x>=0 and x<self.n and y>=0 and y<self.m and self.grid[x][y]==1 and (x,y) not in self.vis:
                self.dfs(x,y)
        
