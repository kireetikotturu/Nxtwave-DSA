"""
Problem: Reverse of an Array
Approach: Recursion with Two-Pointer Swap
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def reverseHelper(self, i, arr, N):
        if i >= N // 2:
            return
        arr[i], arr[N - i - 1] = arr[N - i - 1], arr[i]
        self.reverseHelper(i + 1, arr, N)

    def reverse(self, arr, N):
        self.reverseHelper(0, arr, N)
