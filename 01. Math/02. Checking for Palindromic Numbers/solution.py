"""
Problem: Checking for Palindromic Numbers
Approach: Reverse Number and Compare with Original
Difficulty: Easy
Time Complexity: O(log₁₀N)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, n):
        reversed_number = 0
        n1 = n

        # Reverse the number
        while n1 != 0:
            last_digit = n1 % 10
            reversed_number = reversed_number * 10 + last_digit
            n1 //= 10

        # Check if reversed number matches original
        return reversed_number == n
