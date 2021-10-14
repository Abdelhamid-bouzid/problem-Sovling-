class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        self.g = collections.defaultdict(list)
        N = len(quiet)
        for u,v in richer:
            self.g[v].append(u)
            
        self.quiet = quiet
        self.answer = [None]*N     
        for i in range(N):
            self.dfs(i)
        return self.answer
    
    def dfs(self,node):
        if self.answer[node] is None:
            self.answer[node] = node
            for n in self.g[node]:
                p = self.dfs(n)
                if self.quiet[p]<self.quiet[self.answer[node]]:
                    self.answer[node] = p
        return self.answer[node]
            
