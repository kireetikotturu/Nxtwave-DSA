"""
Problem: Sum of all Digits Between Numbers
Approach: Iterate through range and sum digits using modulo
Difficulty: Easy
Time Complexity: O((N2 − N1 + 1) × log₁₀N2)
Space Complexity: O(1)
"""

class Solution:
    def calculateDigitSum(self, N1, N2):
        total_sum = 0

        for num in range(N1, N2 + 1):
            temp = num
            while temp != 0:
                total_sum += temp % 10
                temp //= 10

        return total_sum
