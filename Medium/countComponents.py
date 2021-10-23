class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        self.g = collections.defaultdict(list)
        for u,v in edges:
            self.g[u].append(v)
            self.g[v].append(u)
            
        all_node = set([i for i in range(n)])
        self.vis = set()
        diff = all_node.difference(self.vis)
        
        count = 0
        while diff:
            start = next(iter(diff))
            self.dfs(start)
            
            diff = all_node.difference(self.vis)
            count +=1
        return count
        
    def dfs(self,node):
        if node in self.vis:
            return
        self.vis.add(node)
        for adj in self.g[node]:
            self.dfs(adj)
        
