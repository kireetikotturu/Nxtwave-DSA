"""
Problem: Largest Odd Number in a String
Approach: Scan from right to left to find the last odd digit
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def largestOddNumber(self, s):
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 == 1:
                return s[:i + 1]
        return ""
