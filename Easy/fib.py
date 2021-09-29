class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        prev = 0
        curr = 1
        for i in range(1,n):
            tmp = curr
            curr = curr+prev
            prev = tmp
        
        return curr
