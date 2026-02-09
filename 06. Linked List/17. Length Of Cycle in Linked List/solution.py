"""
Problem: Length Of Cycle in Linked List
Approach: Floyd’s Cycle Detection (Slow & Fast Pointers)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def lengthOfCycle(self, head):
        slow = head
        fast = head

        # Detect cycle using slow and fast pointers
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                count = 1
                temp = slow.next

                # Count the number of nodes in the cycle
                while temp != slow:
                    temp = temp.next
                    count += 1

                return count

        # No cycle found
        return 0
