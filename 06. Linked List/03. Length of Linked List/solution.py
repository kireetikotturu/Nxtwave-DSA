"""
Problem: Length of Linked List
Approach: Iterative Traversal
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class solution:
    def lengthofLL(self, Node, head):
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        return count
