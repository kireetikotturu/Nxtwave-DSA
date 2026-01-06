"""
Problem: Generalized Fibonacci Sequence
Approach: Recursion with Sliding Window Sum of Last k Elements
Difficulty: Medium
Time Complexity: O(n * k)
Space Complexity: O(n)
"""

class Solution:
    def generateGeneralizedFibonacci(self, k, start, n):
        def solve():
            if len(start) == n:
                return start

            total = 0
            for i in range(len(start) - k, len(start)):
                total += start[i]

            start.append(total)
            return solve()

        return solve()
