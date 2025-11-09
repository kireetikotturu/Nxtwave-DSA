"""
Problem: Find the Second Smallest Element in an Array
Approach: Single Pass (Track smallest and second smallest)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def secondSmallestElement(self, arr, n):
        # Handle edge case: not enough elements
        if n < 2:
            return None

        smallest = float('inf')
        second_smallest = float('inf')

        # Traverse the array once
        for num in arr:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif smallest < num < second_smallest:
                second_smallest = num

        # If second smallest never updated (all elements equal)
        if second_smallest == float('inf'):
            return None

        return second_smallest
