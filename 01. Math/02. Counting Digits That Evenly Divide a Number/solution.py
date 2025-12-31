"""
Problem: Counting Digits That Evenly Divide a Number
Approach: Extract Digits and Check Divisibility
Difficulty: Easy
Time Complexity: O(log₁₀N)
Space Complexity: O(1)
"""

class Solution:
    def evenly_divides(self, N):
        count = 0
        n1 = N

        while n1 != 0:
            digit = n1 % 10
            if digit > 0 and N % digit == 0:
                count += 1
            n1 //= 10

        return count
