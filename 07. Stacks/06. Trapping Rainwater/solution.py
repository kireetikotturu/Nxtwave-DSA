"""
Problem: Trapping Rainwater
Approach: Two Pointer Technique
Difficulty: Hard
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def trapRainwater(self, arr):
        left = 0
        right = len(arr) - 1
        left_max = 0
        right_max = 0
        water = 0

        while left <= right:
            if left_max <= right_max:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                right -= 1

        return water
