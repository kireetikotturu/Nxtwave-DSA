"""
Problem: Move Zeros to the Front of an Array
Approach: Two-Pointer (Reverse Traversal In-place Swap)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZerosToFront(self, arr, n):
        pointer = n - 1  # Pointer to track position for next non-zero element
        
        for i in range(n - 1, -1, -1):
            if arr[i] != 0:
                arr[i], arr[pointer] = arr[pointer], arr[i]
                pointer -= 1
        
        return arr
