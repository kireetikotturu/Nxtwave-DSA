"""
Problem: Find the Largest Element in an Array
Approach: Simple Linear Traversal
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def largestElement(self, arr, n):
        # Initialize the first element as the maximum
        max_num = arr[0]

        # Traverse the array to find the maximum element
        for i in range(n):
            if arr[i] > max_num:
                max_num = arr[i]

        return max_num
