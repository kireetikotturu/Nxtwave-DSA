"""
Problem: Filter Linked List Nodes by Array
Approach: Use a set for quick lookup and remove matching nodes
Difficulty: Medium
Time Complexity: O(n + m)
Space Complexity: O(m)
"""

class Solution:
    def deleteNodes(self, head, arr):
        # Convert array to set for O(1) lookup
        remove_set = set(arr)

        # Dummy node to handle head deletion cases
        dummy = Node(0)
        dummy.next = head

        curr = dummy

        # Traverse the linked list
        while curr.next:
            if curr.next.data in remove_set:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
