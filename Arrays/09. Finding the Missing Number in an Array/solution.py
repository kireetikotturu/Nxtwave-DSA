"""
Problem: Finding the Missing Number in an Array
Approach: XOR Technique (Bit Manipulation)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, arr, n):
        xor1 = 0  # XOR of array elements
        xor2 = 0  # XOR of numbers from 1 to n

        for i in range(n - 1):
            xor1 ^= arr[i]
            xor2 ^= (i + 1)

        # XOR both results with n to find the missing number
        return xor1 ^ xor2 ^ n
