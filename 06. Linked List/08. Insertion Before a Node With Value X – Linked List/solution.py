"""
Problem: Insertion Before a Node With Value X - Linked List
Approach: Traverse list and insert before target node
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def insertionBeforeX(self, head, x, data):
        # If list is empty
        if head is None:
            return None

        # If target is at head
        if head.data == x:
            return Node(data, head)

        temp = head

        # Traverse until the node before target
        while temp.next:
            if temp.next.data == x:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next

        return head
