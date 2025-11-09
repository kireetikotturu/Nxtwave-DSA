"""
Problem: Find the Smallest Element in an Array
Approach: Single Pass (Linear Traversal)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def smallestElement(self, arr, n):
        # Initialize the first element as the smallest
        min_num = arr[0]

        # Traverse the array to find the minimum element
        for i in range(1, n):
            if arr[i] < min_num:
                min_num = arr[i]

        return min_num
