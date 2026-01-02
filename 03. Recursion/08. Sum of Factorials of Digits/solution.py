"""
Problem: Sum of Factorials of Digits
Approach: Recursion on Digits + Recursive Factorial
Difficulty: Medium
Time Complexity: O(d × f)
Space Complexity: O(d)
"""

class Solution:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def sumOfFactorialsOfDigits(self, n):
        if n == 0:
            return 0
        return self.factorial(n % 10) + self.sumOfFactorialsOfDigits(n // 10)
