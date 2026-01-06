"""
Problem: Recursive Power Calculation
Approach: Exponentiation by Squaring (Optimized Recursion)
Difficulty: Medium
Time Complexity: O(log b)
Space Complexity: O(log b)
"""

class Solution:
    def recursivePower(self, a, b):
        if b == 0:
            return 1

        half = self.recursivePower(a, b // 2)

        if b % 2 == 0:
            return half * half
        else:
            return half * half * a
