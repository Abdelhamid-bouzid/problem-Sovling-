class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.g = collections.defaultdict(list)
        for u,v in edges:
            self.g[u].append(v)
            self.g[v].append(u)
        
        for u,v in edges[::-1]:
            self.vis=set()
            self.dfs(1,u,v)
            if len(self.vis)==len(self.g):
                return [u,v]
        
    def dfs(self,node,u,v):
        if node in self.vis:
            return True
        self.vis.add(node)
        
        for adj in self.g[node]:
            if [node,adj]!=[u,v] and [adj,node]!=[u,v]:
                self.dfs(adj,u,v)
