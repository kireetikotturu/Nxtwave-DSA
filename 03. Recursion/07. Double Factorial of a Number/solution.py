"""
Problem: Double Factorial of a Number
Approach: Recursion (n × doubleFactorial(n-2))
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def doubleFactorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.doubleFactorial(n - 2)
