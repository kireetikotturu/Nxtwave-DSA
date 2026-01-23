"""
Problem: String to Integer Conversion (atoi)
Approach: Parse string step-by-step with sign handling and overflow checks
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def stringToInteger(self, s):
        i = 0
        n = len(s)
        sign = 1
        ans = 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Handle sign
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Convert digits
        while i < n and '0' <= s[i] <= '9':
            ans = ans * 10 + (ord(s[i]) - ord('0'))

            # Overflow handling
            if sign * ans >= INT_MAX:
                return INT_MAX
            if sign * ans <= INT_MIN:
                return INT_MIN

            i += 1

        return sign * ans
