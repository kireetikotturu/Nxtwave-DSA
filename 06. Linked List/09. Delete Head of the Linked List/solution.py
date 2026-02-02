"""
Problem: Delete Head of the Linked List
Approach: Move the head pointer to the next node
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def deleteHead(self, head):
        # If the linked list is empty
        if head is None:
            return None

        # Move head to the next node
        return head.next
