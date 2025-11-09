"""
Problem: Second Largest Element in an Array
Approach: Single Pass (Track largest and second largest)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def secondLargestElement(self, arr, n):
        if n < 2:
            return None  # Not enough elements for second largest

        largest = float('-inf')
        second_largest = float('-inf')

        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif largest > num > second_largest:
                second_largest = num

        # Handle case where all elements are the same
        if second_largest == float('-inf'):
            return None

        return second_largest
