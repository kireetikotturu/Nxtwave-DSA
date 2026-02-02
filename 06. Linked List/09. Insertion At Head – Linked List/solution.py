"""
Problem: Insertion At Head - Linked List
Approach: Create a new node and point it to the current head
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def insertionAtHead(self, head, a):
        # Create a new node
        new_node = Node(a)

        # Point new node to current head
        new_node.next = head

        # New node becomes the head
        return new_node
