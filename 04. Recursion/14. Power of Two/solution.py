"""
Problem: Power of Two
Approach: Recursion by dividing n by 2
Difficulty: Easy
Time Complexity: O(log N)
Space Complexity: O(log N)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        return n % 2 == 0 and self.isPowerOfTwo(n // 2)
