"""
Problem: Checking for Prime Numbers
Approach: Count Divisors Using √N Optimization
Difficulty: Easy
Time Complexity: O(√N)
Space Complexity: O(1)
"""

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False

        count = 0
        i = 1

        while i <= int(n ** 0.5):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
            i += 1

        return count == 2
