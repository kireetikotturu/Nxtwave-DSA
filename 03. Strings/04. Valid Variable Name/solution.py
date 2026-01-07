"""
Problem: Valid Variable Name
Approach: Check Unicode value of each character
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def isValidVariableName(self, s):
        for ch in s:
            if not (
                65 <= ord(ch) <= 90 or
                97 <= ord(ch) <= 122 or
                48 <= ord(ch) <= 57
            ):
                return False
        return True
