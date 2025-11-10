"""
Problem: Move Zeros to the End of an Array
Approach: Two-Pointer (In-place Swap)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZerosToEnd(self, arr, n):
        pointer = 0  # Position to place the next non-zero element
        
        for i in range(n):
            if arr[i] != 0:
                arr[pointer], arr[i] = arr[i], arr[pointer]
                pointer += 1
        
        return arr
