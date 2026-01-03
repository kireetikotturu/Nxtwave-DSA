"""
Problem: Factorial Sequence using Recursion
Approach: Build factorial list recursively using previous result
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def factorialSequence(self, n):
        if n == 1:
            return [1]

        result = self.factorialSequence(n - 1)
        result.append(n * result[-1])
        return result
