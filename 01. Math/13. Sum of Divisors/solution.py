"""
Problem: Sum of Divisors
Approach: Iterate up to √N and add divisor pairs directly
Difficulty: Medium
Time Complexity: O(√N)
Space Complexity: O(1)
"""

class Solution:
    def sumOfDivisors(self, num):
        divisors_sum = 0

        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i

        return divisors_sum
