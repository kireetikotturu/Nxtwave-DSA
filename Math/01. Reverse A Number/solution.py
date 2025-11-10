"""
Problem: Reverse A Number
Approach: Mathematical Reversal Using Modulus and Division
Difficulty: Easy
Time Complexity: O(log₁₀N)
Space Complexity: O(1)
"""

class Solution:
    def reverseNumber(self, N):
        reversed_number = 0

        while N != 0:
            last_digit = N % 10
            reversed_number = last_digit + reversed_number * 10
            N //= 10

        return reversed_number
