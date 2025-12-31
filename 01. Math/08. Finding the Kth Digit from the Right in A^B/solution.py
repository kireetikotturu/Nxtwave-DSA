"""
Problem: Finding the Kth Digit from the Right in A^B
Approach: Compute Power and Extract Digits Using Modulo
Difficulty: Easy
Time Complexity: O(B + K)
Space Complexity: O(1)
"""

class Solution:
    def kthDigit(self, A, B, k):
        power = A ** B

        while k > 0:
            digit = power % 10
            power //= 10
            k -= 1

        return digit
