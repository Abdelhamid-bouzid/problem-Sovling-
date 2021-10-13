class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        # transform the graph to adjacent because it is faster on dfs
        g = [[] for i in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        
        self.g = g
        self.end = end
        self.visited = []
        return self.dfs(start)
        
        
    def dfs(self,node):
        if node==self.end:
            return True
        if node in self.visited:
            return False
        
        self.visited.append(node)
        for n in self.g[node]:
            if self.dfs(n):
                return True
            
