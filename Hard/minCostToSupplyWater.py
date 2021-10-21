class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        
        g = collections.defaultdict(list)
        for u,v,w in pipes:
            g[u].append([v,w])
            g[v].append([u,w])
            
        for index,w in enumerate(wells):
            g[0].append([index+1,w])
            
        vis = set([0])
        q = [(w,0,dst) for dst,w in g[0]]
        heapq.heapify(q)
        
        cost = 0
        while q:
            c,node,dst = heapq.heappop(q)
            if dst in vis:
                continue
            vis.add(dst)
            
            cost +=c
            for adj,w in g[dst]:
                if adj not in vis:
                    heapq.heappush(q,(w,dst,adj))
                    
        return cost
