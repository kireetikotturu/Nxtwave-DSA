"""
Problem: Linked List Traversal
Approach: Iterative Traversal using Pointer
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class solution:
    def traversal(self, Node, head):
        current = head
        result = []

        while current:
            result.append(current.data)
            current = current.next

        print(*result)
