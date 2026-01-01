"""
Problem: Sum of Digits Until Single Digit
Approach: Digital Root (Mathematical Formula)
Difficulty: Medium
Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def sumOfDigits(self, num):
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9
