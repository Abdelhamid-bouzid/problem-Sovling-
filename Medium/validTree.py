class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1: return False

        # Create an adjacency list.
        self.adj_list = [[] for _ in range(n)]
        for A, B in edges:
            self.adj_list[A].append(B)
            self.adj_list[B].append(A)

        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        self.seen = set()
        self.dfs(0)
        return len(self.seen) == n
    
    def dfs(self,node):
        if node in self.seen: 
            return
        self.seen.add(node)
        for neighbour in self.adj_list[node]:
            self.dfs(neighbour)
