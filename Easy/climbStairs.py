import functools

class Solution:
    @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else 2 if n == 2 else 1
