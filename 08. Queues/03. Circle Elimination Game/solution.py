"""
Problem: Circle Elimination Game
Approach: Queue Rotation using Deque
Difficulty: Medium
Time Complexity: O(N * K)
Space Complexity: O(N)
"""

from collections import deque

class Solution:
    def getCircleWinner(self, n, k):
        circle = deque(range(1, n + 1))

        while len(circle) > 1:
            for _ in range(k - 1):
                circle.append(circle.popleft())
            circle.popleft()

        return circle[0]
