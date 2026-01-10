"""
Problem: Balanced Parenthesis
Approach: Stack-based matching of brackets
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def balancedParentheses(self, s):
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False

                top = stack.pop()
                if (
                    (ch == ")" and top == "(") or
                    (ch == "}" and top == "{") or
                    (ch == "]" and top == "[")
                ):
                    continue
                else:
                    return False

        return not stack
