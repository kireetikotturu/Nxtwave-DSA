"""
Problem: Union of Two Sorted Arrays
Approach: Two-Pointer Merge Technique
Difficulty: Medium
Time Complexity: O(m + n)
Space Complexity: O(m + n)
"""

class Solution:
    def unionOfTwoSortedArrays(self, a, b):
        union = []
        pointer_1, pointer_2 = 0, 0

        # Traverse both arrays simultaneously
        while pointer_1 < len(a) and pointer_2 < len(b):
            if a[pointer_1] < b[pointer_2]:
                if not union or a[pointer_1] != union[-1]:
                    union.append(a[pointer_1])
                pointer_1 += 1
            else:
                if not union or b[pointer_2] != union[-1]:
                    union.append(b[pointer_2])
                pointer_2 += 1

        # Process remaining elements in array a
        while pointer_1 < len(a):
            if not union or a[pointer_1] != union[-1]:
                union.append(a[pointer_1])
            pointer_1 += 1

        # Process remaining elements in array b
        while pointer_2 < len(b):
            if not union or b[pointer_2] != union[-1]:
                union.append(b[pointer_2])
            pointer_2 += 1

        return union
