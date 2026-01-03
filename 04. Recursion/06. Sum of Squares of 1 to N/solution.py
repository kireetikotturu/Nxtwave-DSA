"""
Problem: Sum of Squares of 1 to N
Approach: Recursion (n² + sumOfSquares(n-1))
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def recursiveSumOfSquares(self, n):
        if n == 1:
            return 1
        return n * n + self.recursiveSumOfSquares(n - 1)
