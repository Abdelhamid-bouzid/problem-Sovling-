class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges)==0:
            return [0]
        
        g = [[] for i in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        degree = [0]*n
        for i in range(n):
            degree[i] = len(g[i])
            
        leaves = []
        while len(leaves)<len(g):
            next_leaves = []
            for j,node in enumerate(g):
                if degree[j]==1:
                    next_leaves.append(j)
                    degree[j] -=1
            leaves.extend(next_leaves)
            for j in next_leaves:
                for adj in g[j]:
                    if degree[adj]>1:
                        degree[adj] -=1
        return next_leaves
