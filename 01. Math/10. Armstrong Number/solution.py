"""
Problem: Armstrong Number
Approach: Digit Extraction and Power Sum
Difficulty: Medium
Time Complexity: O(log₁₀N)
Space Complexity: O(1)
"""

class Solution:
    def checkArmstrongNumber(self, num):
        total = 0
        digits = len(str(num))
        temp = num

        while temp > 0:
            digit = temp % 10
            total += digit ** digits
            temp //= 10

        return total == num
