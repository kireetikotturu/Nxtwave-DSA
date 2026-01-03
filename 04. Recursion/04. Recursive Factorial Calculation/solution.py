"""
Problem: Recursive Factorial Calculation
Approach: Recursion (N * factorial(N-1))
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def recursionFactorial(self, n):
        if n <= 1:
            return 1
        return n * self.recursionFactorial(n - 1)
