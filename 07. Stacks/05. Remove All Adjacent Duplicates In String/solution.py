"""
Problem: Remove All Adjacent Duplicates In String
Approach: Stack (Remove duplicates when top matches current character)
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
