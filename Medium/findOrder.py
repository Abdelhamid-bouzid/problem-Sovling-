class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        g = collections.defaultdict(list)
        indergree = [0]*numCourses
        for u,v in prerequisites:
            g[v].append(u)
            indergree[u] +=1
        
        classes = []
        for i in range(numCourses):
            next_class = -1
            for j in range(numCourses):
                if indergree[j]==0:
                    next_class = j
                    break
                    
            if next_class==-1:
                return []
            else:
                indergree[j] = -1
                classes.append(j)
                for n in g[j]:
                    indergree[n] -=1
                
        return classes
