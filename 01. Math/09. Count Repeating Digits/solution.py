"""
Problem: Count Repeating Digits
Approach: Frequency Count Using Array
Difficulty: Medium
Time Complexity: O(log₁₀N)
Space Complexity: O(1)
"""

class Solution:
    def countRepeatingDigits(self, num):
        count = [0] * 10
        result = 0

        while num > 0:
            digit = num % 10
            count[digit] += 1
            num //= 10

        for freq in count:
            if freq > 1:
                result += 1

        return result
