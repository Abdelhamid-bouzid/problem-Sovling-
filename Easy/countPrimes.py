'''
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        i=0
        while n>1:
            n -=1
            if self.is_prime(n):
                i +=1
        return i
            
    def is_prime(self,n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        # since all primes > 3 are of the form 6n ± 1
        # start with f=5 (which is prime)
        # and test f, f+2 for being prime
        # then loop by 6. 
        f = 5
        while f <= r:
            if n % f == 0: return False
            if n % (f+2) == 0: return False
            f += 6
        return True
