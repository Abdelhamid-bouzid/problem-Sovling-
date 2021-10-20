class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        g = collections.defaultdict(list)
        for el,p in zip(edges,succProb):
            u,v=el[0],el[1]
            g[u].append([v,p])
            g[v].append([u,p])
        
        distance = [0]*n
        distance[start] = 1
        processed = [False]*n
        
        hq = [(-1,start)]
        
        while hq:
            cur_p,node = heapq.heappop(hq)
            if processed[node]:
                continue
            processed[node] = True
            
            for adj,p in g[node]:
                if -cur_p*p>distance[adj]:
                    distance[adj] = -cur_p*p
                    heapq.heappush(hq,(cur_p*p,adj))
            
        #print(distance)
        return distance[end]
