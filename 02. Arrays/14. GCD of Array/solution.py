
"""
Problem: GCD of Array
Approach: Iterative GCD (Euclidean Algorithm)
Difficulty: Easy
Time Complexity: O(N * log(min(arr[i])))
Space Complexity: O(1)
"""

class Solution:
    def gcd_of_two(self, a, b):
        # Euclidean algorithm to find GCD of two numbers
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return b if a == 0 else a

    def gcd(self, N, arr):
        gcd = arr[0]
        for i in range(1, len(arr)):
            gcd = self.gcd_of_two(gcd, arr[i])
        return gcd
