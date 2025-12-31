"""
Problem: Automorphic Number
Approach: Compare Digits of Number with its Square from Right to Left
Difficulty: Medium
Time Complexity: O(log₁₀N)
Space Complexity: O(1)
"""

class Solution:
    def checkAutomorphicNumber(self, num):
        num_sq = num * num

        while num > 0:
            if num % 10 != num_sq % 10:
                return False
            num //= 10
            num_sq //= 10

        return True
