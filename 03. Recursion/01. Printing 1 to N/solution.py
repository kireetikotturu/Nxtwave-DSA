"""
Problem: Printing 1 to N
Approach: Recursion (Incremental Call)
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def helperFunction(self, i, n):
        if i == n + 1:
            return
        print(i)
        self.helperFunction(i + 1, n)

    def print1toNInAscendingOrder(self, N):
        self.helperFunction(1, N)
