"""
Problem: Find the Second Largest Element in an Array
Approach: Single Pass (Track largest and second largest)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
Companies: SAP
"""

class Solution:
    def secondLargestElement(self, arr, n):
        # Handle edge case: not enough elements
        if n < 2:
            return None

        largest = float('-inf')
        second_largest = float('-inf')

        # Traverse the array once
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif largest > num > second_largest:
                second_largest = num

        # If second largest never updated (all elements equal)
        if second_largest == float('-inf'):
            return None

        return second_largest
