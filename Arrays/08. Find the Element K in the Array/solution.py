"""
Problem: Find the Element K in the Array
Approach: Linear Search (Iterative Traversal)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def search(self, arr, n, k):
        for i in range(n):
            if arr[i] == k:
                return i
        return -1
