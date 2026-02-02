"""
Problem: Insertion At Tail - Linked List
Approach: Traverse to the last node and attach the new node
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def insertionAtTail(self, head, a):
        # If the list is empty, new node becomes the head
        if head is None:
            return Node(a)

        # Traverse to the last node
        temp = head
        while temp.next:
            temp = temp.next

        # Insert new node at the end
        temp.next = Node(a)

        return head
