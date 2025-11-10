"""
Problem: Remove Duplicates from Sorted Array
Approach: Two Pointer Technique (In-place Overwrite)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, arr, n):
        # If the array has 0 or 1 element, it is already unique
        if n <= 1:
            return n

        j = 0  # Pointer for last unique element

        # Traverse through the array
        for i in range(1, n):
            if arr[j] != arr[i]:
                j += 1
                arr[j] = arr[i]

        # Return count of unique elements
        return j + 1
