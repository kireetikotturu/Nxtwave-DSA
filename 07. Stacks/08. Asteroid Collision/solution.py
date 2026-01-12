"""
Problem: Asteroid Collision
Approach: Stack Simulation
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def asteroidCollision(self, arr):
        stack = []

        for asteroid in arr:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] + asteroid < 0:
                    stack.pop()

                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] + asteroid == 0:
                    stack.pop()

        return stack
