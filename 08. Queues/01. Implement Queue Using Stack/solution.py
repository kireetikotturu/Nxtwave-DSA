"""
Problem: Implement Queue Using Stack
Approach: Two Stack Reversal Method
Difficulty: Easy
Time Complexity:
- push: O(N)
- pop: O(1)
- front: O(1)
- back: O(N)
Space Complexity: O(N)
"""

class MyQueue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x):
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        self.stk1.append(x)
        while self.stk2:
            self.stk1.append(self.stk2.pop())

    def pop(self):
        if self.stk1:
            self.stk1.pop()

    def front(self):
        if self.stk1:
            return self.stk1[-1]
        return -1

    def back(self):
        if not self.stk1:
            return -1
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        val = self.stk2[-1]
        while self.stk2:
            self.stk1.append(self.stk2.pop())
        return val

    def size(self):
        return len(self.stk1)

    def empty(self):
        return len(self.stk1) == 0
