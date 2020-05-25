# runtime complexity: O(n^2) because of the for loop and the while loop
# space time complexity: O(n) additional space because we allocate a boolan array of size n
class Solution:
    def countPrimes(self, n: int) -> int:
        # boolean list where everything is false
        l = [False] * n
        # counter for keeping track of primes
        count = 0
        
        for i in range(2, n):
            if l[i] == False:
                count += 1
                j = 2
                while i * j < n:
                    l[i * j] = True
                    j += 1
        return count