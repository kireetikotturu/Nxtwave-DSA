"""
Problem: Check if an Array is Sorted
Approach: Single Pass (Compare consecutive elements)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isSorted(self, arr, n):
        # Traverse the array and compare adjacent elements
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                return False
        return True
