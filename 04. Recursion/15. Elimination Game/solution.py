"""
Problem: Elimination Game
Approach: Recursive Mathematical Simulation
Difficulty: Medium
Time Complexity: O(log N)
Space Complexity: O(log N)
"""

class Solution:
    def lastRemaining(self, n: int) -> int:
        def solve(remaining, step, head, leftToRight):
            if remaining == 1:
                return head

            # Update head if elimination starts from left
            # OR when eliminating from right with odd count
            if leftToRight or remaining % 2 == 1:
                head += step

            return solve(
                remaining // 2,
                step * 2,
                head,
                not leftToRight
            )

        return solve(n, 1, 1, True)
