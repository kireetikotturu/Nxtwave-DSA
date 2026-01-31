"""
Problem: Convert Array To Linked List
Approach: Iterative Linked List Construction
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class solution:
    def arrayToLL(self, Node, n, arr):
        if n == 0:
            return None

        head = Node(arr[0])
        current = head

        for value in arr[1:]:
            current.next = Node(value)
            current = current.next

        return head
