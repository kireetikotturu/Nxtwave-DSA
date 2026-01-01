"""
Problem: LCM of an Array
Approach: Iteratively compute LCM using GCD (LCM = a*b / GCD)
Difficulty: Easy
Time Complexity: O(n · log(max(arr[i])))
Space Complexity: O(1)
"""

class Solution:
    def lcmArray(self, arr):
        MOD = 10**9 + 7

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        def lcm(a, b):
            return (a * b) // gcd(a, b) % MOD

        current_lcm = arr[0]
        for i in range(1, len(arr)):
            current_lcm = lcm(current_lcm, arr[i])

        return current_lcm
