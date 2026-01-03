"""
Problem: Print 1-N & Back with Conditions
Approach: Recursion with Pre-order and Post-order Printing
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def helperFunction(self, i, n):
        if i == n + 1:
            return

        # Pre-recursion: print even numbers in ascending order
        if i % 2 == 0:
            print(i, end=" ")

        self.helperFunction(i + 1, n)

        # Post-recursion: print odd numbers in descending order
        if i % 2 != 0:
            print(i, end=" ")

    def printEvenOdd(self, n):
        self.helperFunction(1, n)
