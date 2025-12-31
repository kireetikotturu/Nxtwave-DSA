"""
Problem: Sum of Divisors
Approach: Iterate up to √N and add divisor pairs
Difficulty: Medium
Time Complexity: O(√N)
Space Complexity: O(√N)
"""

class Solution:
    def sumOfDivisors(self, num):
        divisors_list = []

        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors_list.append(i)
                if i != num // i:
                    divisors_list.append(num // i)

        return sum(divisors_list)
