"""
Problem: Nth Fibonacci Number
Approach: Recursive Definition (fib(n) = fib(n-1) + fib(n-2))
Difficulty: Easy
Time Complexity: O(2^N)
Space Complexity: O(N)
"""

class Solution:
    def fibNum(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fibNum(N - 1) + self.fibNum(N - 2)
