"""
Problem: Max Nesting Depth in Parentheses
Approach: Count open parentheses and track maximum depth
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def maxNestingDepth(self, s):
        current_depth = 0
        max_depth = 0

        for ch in s:
            if ch == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif ch == ')':
                current_depth -= 1

        return max_depth
