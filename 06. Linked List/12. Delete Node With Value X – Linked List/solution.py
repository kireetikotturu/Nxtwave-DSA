"""
Problem: Delete Node With Value X – Linked List
Approach: Traverse the list and remove the first node with value x
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def deleteNodeWithValueX(self, head, x):
        # If the list is empty
        if head is None:
            return None

        # If the head node contains value x
        if head.data == x:
            return head.next

        curr = head

        # Traverse the list to find value x
        while curr.next:
            if curr.next.data == x:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head
