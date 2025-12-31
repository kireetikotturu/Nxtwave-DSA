"""
Problem: Perfect Number
Approach: Sum Proper Divisors Using √N Optimization
Difficulty: Easy
Time Complexity: O(√N)
Space Complexity: O(1)
"""

class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        divisors_sum = 1  # 1 is always a proper divisor

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i

        return divisors_sum == num
