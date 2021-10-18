class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        g = collections.defaultdict(list)
        for i,el in enumerate(equations):
            u,v = el[0],el[1]
            g[u].append([v,values[i]])
            g[v].append([u,1/values[i]])
            
        ans = []
        for u,v in queries:
            if u not in g.keys() or v not in g.keys():
                ans.append(-1)
            else:
                ans.append(self.dijkstra(u,v,g))
            
        return ans
            
        
    def dijkstra(self,start, end,g):
        processed = {}
        distance = {}
        for key in g:
            processed[key] = False
            distance[key]  = 1
        
        distance[start] = 1
        
        q = collections.deque([start])
        while q:
            node = q.pop()
            if processed[node]:
                continue
            processed[node] = True
            for adj,v in g[node]:
                distance[adj] = distance[node]*v
                q.append(adj)
        
        
        if not processed[end]:
            return -1
        else:
            return distance[end]
