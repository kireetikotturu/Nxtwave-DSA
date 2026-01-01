"""
Problem: Finding the Greatest Common Divisor of Two Numbers
Approach: Euclidean Algorithm (Modulo-based)
Difficulty: Easy
Time Complexity: O(log(min(A, B)))
Space Complexity: O(1)
"""

class Solution:
    def gcd(self, A, B):
        while A != 0 and B != 0:
            if A >= B:
                A = A % B
            else:
                B = B % A
        return B if A == 0 else A
