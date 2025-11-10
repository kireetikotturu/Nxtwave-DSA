"""
Problem: Maximum Consecutive Ones in an Array
Approach: Linear Scan (Counting Consecutive 1s)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxConsecutiveOnes(self, arr, n):
        max_c = 0       # Stores maximum consecutive 1s
        current = 0     # Current count of consecutive 1s

        for i in arr:
            if i == 1:
                current += 1
                if max_c < current:
                    max_c = current
            else:
                current = 0

        return max_c
