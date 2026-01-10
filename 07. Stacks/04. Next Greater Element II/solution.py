"""
Problem: Next Greater Element II
Approach: Circular Monotonic Stack (Traverse 2N times)
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def nextGreaterElementII(self, arr):
        n = len(arr)
        ans = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            while stack and arr[i % n] >= stack[-1]:
                stack.pop()

            if i < n and stack:
                ans[i] = stack[-1]

            stack.append(arr[i % n])

        return ans
