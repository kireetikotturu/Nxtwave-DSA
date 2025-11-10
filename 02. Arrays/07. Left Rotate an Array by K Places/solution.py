"""
Problem: Left Rotate an Array by K Places
Approach: Reverse Sub-array Method (Three-step reversal)
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def leftRotate(self, arr, n, k):
        # Normalize k to avoid full rotations
        k = k % n
        if k == 0:
            return arr

        # Reverse the first k elements
        self.reverse(arr, 0, k - 1)
        # Reverse the remaining n − k elements
        self.reverse(arr, k, n - 1)
        # Reverse the whole array
        self.reverse(arr, 0, n - 1)
        return arr
