"""
Problem: Count the Number of Digits
Approach: Repeated Division by 10
Difficulty: Easy
Time Complexity: O(log₁₀N)
Space Complexity: O(1)
"""

class Solution:
    def countDigits(self, n):
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count
