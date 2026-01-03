"""
Problem: Reversing Array Sections
Approach: Recursion with Two-Pointer Swap (Section Only)
Difficulty: Easy
Time Complexity: O(right - left + 1)
Space Complexity: O(right - left + 1)
"""

class Solution:
    def reverseArraySection(self, arr, n, left, right):
        if left >= right:
            return
        arr[left], arr[right] = arr[right], arr[left]
        self.reverseArraySection(arr, n, left + 1, right - 1)
