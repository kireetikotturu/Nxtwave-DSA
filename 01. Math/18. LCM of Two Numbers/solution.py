"""
Problem: LCM of Two Numbers
Approach: Use GCD (LCM = (A × B) / GCD)
Difficulty: Easy
Time Complexity: O(log(min(A, B)))
Space Complexity: O(1)
"""

class Solution:
    def lcm(self, A, B):
        def gcd(x, y):
            while x != 0 and y != 0:
                if x > y:
                    x = x % y
                else:
                    y = y % x
            return y if x == 0 else x

        return (A * B) // gcd(A, B)
