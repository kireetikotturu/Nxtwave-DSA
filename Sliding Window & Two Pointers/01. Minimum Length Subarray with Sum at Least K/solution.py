"""
Problem: Minimum Length Subarray with Sum at Least K
Approach: Sliding Window (Two Pointers)
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def minSubArrayLen(self, k, arr):
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(arr)):
            current_sum += arr[right]

            while current_sum >= k:
                min_length = min(min_length, right - left + 1)
                current_sum -= arr[left]
                left += 1

        return 0 if min_length == float('inf') else min_length
