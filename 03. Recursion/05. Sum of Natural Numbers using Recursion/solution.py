"""
Problem: Sum of Natural Numbers using Recursion
Approach: Recursion (N + sum(N-1))
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def recursionSum(self, N):
        if N == 1:
            return 1
        return N + self.recursionSum(N - 1)
