class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        g = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for u,v in prerequisites:
            g[v].append(u)
            indegree[u] +=1 
            
        for i in range(numCourses):
            Indegreezero = False
            for j in range(numCourses):
                if indegree[j]==0:
                    Indegreezero = True
                    break
            
            if not Indegreezero:
                return False
            indegree[j] = -1
            for node in g[j]:
                indegree[node] -=1
        return True
            
