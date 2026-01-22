"""
Problem: Roman Number to Integer
Approach: Traverse from right to left and apply subtraction logic
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def romanToInteger(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev = 0

        for ch in reversed(s):
            value = roman_map[ch]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total
