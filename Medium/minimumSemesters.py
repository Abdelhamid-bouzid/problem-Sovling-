class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        
        g = collections.defaultdict(list)
        indegree = [0]*n
        for u,v in relations:
            g[u].append(v)
            indegree[v-1] +=1
        
        count = 0
        total = 0
        for i in range(n):
            courses_term = []
            for k,d in enumerate(indegree):
                if d==0:
                    courses_term.append(k+1)
            if len(courses_term)==0:
                return -1
            else:
                count+=1
                total +=len(courses_term)
                if total==n:
                    return count
                for node in courses_term:
                    indegree[node-1] -=1
                    for adj in g[node]:
                        indegree[adj-1] -=1
