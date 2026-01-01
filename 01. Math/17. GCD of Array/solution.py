"""
Problem: GCD of Array
Approach: Iteratively apply Euclidean Algorithm
Difficulty: Easy
Time Complexity: O(N · log(min(arr[i])))
Space Complexity: O(1)
"""

class Solution:
    def gcd_of_two(self, a, b):
        # Euclidean Algorithm
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return b if a == 0 else a

    def gcd(self, N, arr):
        if N == 1:
            return arr[0]

        current_gcd = arr[0]
        for i in range(1, N):
            current_gcd = self.gcd_of_two(current_gcd, arr[i])

        return current_gcd
