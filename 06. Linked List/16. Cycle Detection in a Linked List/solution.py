"""
Problem: Cycle Detection in a Linked List
Approach: Floyd’s Cycle Detection Algorithm (Slow & Fast Pointers)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def cycleDetection(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                return True

        return False
