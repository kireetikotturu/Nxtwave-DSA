"""
Problem: Find Start Node of a Cycle in Linked List
Approach: Floyd’s Cycle Detection + Pointer Reset
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def startNodeCycle(self, head):
        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Step 2: Find start of the cycle
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        # No cycle found
        return None
