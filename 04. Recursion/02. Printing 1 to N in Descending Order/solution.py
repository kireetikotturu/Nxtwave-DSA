"""
Problem: Printing 1 to N in Descending Order
Approach: Recursion (Decremental Call)
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def helperFunction(self, N):
        if N == 0:
            return
        print(N)
        self.helperFunction(N - 1)

    def print1toNInDescendingOrder(self, N):
        self.helperFunction(N)
