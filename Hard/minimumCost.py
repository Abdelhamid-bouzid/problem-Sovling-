class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        g = collections.defaultdict(list)
        for u,v,w in connections:
            g[u].append([v,w])
            g[v].append([u,w])
            
        vis = set([1])
        q = [(w,1,v) for v,w in g[1]]
        heapq.heapify(q)
        
        cost = 0
        while q:
            w,node,dst = heapq.heappop(q)
            if dst in vis:
                continue
            vis.add(dst)
            
            cost +=w
            for adj,w in g[dst]:
                if adj not in vis:
                    heapq.heappush(q,(w,dst,adj))
        if len(vis)<n:
            return -1
        else:
            return cost
                
        
