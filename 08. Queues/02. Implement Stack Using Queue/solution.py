"""
Problem: Implement Stack Using Queue
Approach: Single Queue Rotation
Difficulty: Easy
Time Complexity:
- push: O(N)
- pop: O(1)
- top: O(1)
Space Complexity: O(N)
"""

from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        n = len(self.q)
        self.q.append(x)
        for _ in range(n):
            self.q.append(self.q.popleft())

    def pop(self):
        if self.q:
            self.q.popleft()

    def top(self):
        if self.q:
            return self.q[0]
        return -1

    def empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)
