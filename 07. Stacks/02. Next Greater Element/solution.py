"""
Problem: Next Greater Element
Approach: Monotonic Stack (Right to Left)
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def nextGreaterElement(self, arr):
        stack = []
        result = [-1] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(arr[i])

        return result
