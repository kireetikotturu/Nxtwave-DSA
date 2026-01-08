"""
Problem: Remove Outermost Parentheses
Approach: Balance counter to track primitive depth
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def removeOutermostParentheses(self, s):
        count = 0
        result = []

        for ch in s:
            if ch == "(":
                if count > 0:
                    result.append("(")
                count += 1
            else:
                count -= 1
                if count > 0:
                    result.append(")")

        return "".join(result)
