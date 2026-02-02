"""
Problem: Delete Tail of the Linked List
Approach: Traverse to the second last node and remove its next pointer
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def deleteTail(self, head):
        # If the list is empty or has only one node
        if head is None or head.next is None:
            return None

        # Traverse to the second last node
        curr = head
        while curr.next.next:
            curr = curr.next

        # Remove the last node
        curr.next = None

        return head
