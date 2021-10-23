class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])
        self.vis = set()
        count = 0
        all_shapes = []
        for i in range(self.n):
            for j in range(self.m):
                if (i,j) not in self.vis and self.grid[i][j]==1:
                    self.shape = [[0,0]]
                    self.dfs(i,j,0,0)
                    print(self.shape)
                    exist = False
                    for el in all_shapes:
                        if el==self.shape:
                            exist = True
                            break
                    if not exist:
                        count +=1
                        all_shapes.append(self.shape)
        return count
        
    def dfs(self,i,j,o1,o2):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        self.vis.add((i,j))
        
        for dirc in directions:
            x = i+dirc[0]
            y = j+dirc[1]
            if x>=0 and x<self.n and y>=0 and y<self.m and self.grid[x][y]==1 and (x,y) not in self.vis:
                self.shape.append([o1+dirc[0],o2+dirc[1]])
                self.dfs(x,y,o1+dirc[0],o2+dirc[1])
        
