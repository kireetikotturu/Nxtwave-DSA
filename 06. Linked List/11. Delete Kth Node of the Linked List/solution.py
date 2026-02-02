"""
Problem: Delete Kth Node of the Linked List
Approach: Traverse to the (k-1)th node and adjust pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def deleteKthNode(self, head, k):
        # If the list is empty
        if head is None:
            return None

        # If the head needs to be deleted
        if k == 0:
            return head.next

        curr = head
        count = 0

        # Traverse to the (k-1)th node
        while curr and curr.next:
            if count == k - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1

        return head
