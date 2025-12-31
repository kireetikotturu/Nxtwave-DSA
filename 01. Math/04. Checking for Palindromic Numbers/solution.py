"""
Problem: Checking for Palindromic Numbers
Approach: Reverse the Number and Compare
Difficulty: Easy
Time Complexity: O(log₁₀N)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, n):
        reversed_number = 0
        n1 = n

        while n1 != 0:
            last_digit = n1 % 10
            reversed_number = reversed_number * 10 + last_digit
            n1 //= 10

        return reversed_number == n
