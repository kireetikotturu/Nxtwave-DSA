"""
Problem: Search In Linked List
Approach: Linear Traversal
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class solution:
    def searchInLL(self, Node, head, k):
        current = head

        while current:
            if current.data == k:
                return 1
            current = current.next

        return 0
