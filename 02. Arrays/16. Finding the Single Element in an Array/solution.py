"""
Problem: Finding the Single Element in an Array
Approach: XOR Technique
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findSingleElement(self, arr, n):
        x = 0
        # XOR all elements — duplicates cancel out, leaving the single element
        for i in range(n):
            x ^= arr[i]
        return x
