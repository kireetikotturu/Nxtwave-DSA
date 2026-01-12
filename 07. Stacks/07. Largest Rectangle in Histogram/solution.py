"""
Problem: Largest Rectangle in Histogram
Approach: Monotonic Increasing Stack
Difficulty: Hard
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def largestRectangleArea(self, arr):
        stack = []
        max_area = 0
        n = len(arr)

        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                height = arr[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_area = max(max_area, height * width)
            stack.append(i)

        while stack:
            height = arr[stack.pop()]
            if stack:
                width = n - stack[-1] - 1
            else:
                width = n
            max_area = max(max_area, height * width)

        return max_area
