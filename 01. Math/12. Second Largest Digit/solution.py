"""
Problem: Second Largest Digit
Approach: Track Largest and Second Largest Digit in One Pass
Difficulty: Medium
Time Complexity: O(log₁₀N)
Space Complexity: O(1)
"""

class Solution:
    def secondLargestDigit(self, num):
        first_largest = -1
        second_largest = -1

        while num > 0:
            digit = num % 10

            if digit > first_largest:
                second_largest = first_largest
                first_largest = digit
            elif first_largest > digit > second_largest:
                second_largest = digit

            num //= 10

        return second_largest
