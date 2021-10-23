class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        self.g = collections.defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected[0])):
                if isConnected[i][j]==1:
                    self.g[i].append(j)
                    self.g[j].append(i)
            
        all_node = set([i for i in range(len(isConnected))])
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
