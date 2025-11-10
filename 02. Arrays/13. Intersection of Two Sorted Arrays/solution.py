"""
Problem: Intersection of Two Sorted Arrays
Approach: Two-Pointer (Linear Traversal)
Difficulty: Easy
Time Complexity: O(m + n)
Space Complexity: O(min(m, n))
"""

class Solution:
    def intersectionSortedArrays(self, a, b):
        m, n = len(a), len(b)
        intersection = []
        i, j = 0, 0

        # Traverse both arrays simultaneously
        while i < m and j < n:
            if a[i] == b[j]:
                intersection.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1

        return intersection
