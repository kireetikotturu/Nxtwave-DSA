"""
Problem: Printing Divisors of an Integer in Ascending Order
Approach: Iterate up to √N and collect divisor pairs
Difficulty: Easy
Time Complexity: O(√N)
Space Complexity: O(√N)
"""

class Solution:
    def printDivisors(self, n):
        divisors_list = []

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors_list.append(i)
                if i != n // i:
                    divisors_list.append(n // i)

        divisors_list.sort()
        return divisors_list
