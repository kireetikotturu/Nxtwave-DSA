"""
Problem: Middle of the Linked List
Approach: Two Pointer Technique (Slow & Fast)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def middleOfTheLL(self, head):
        slow = head
        fast = head

        # Move fast pointer twice as fast as slow
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Slow pointer will be at the middle
        return slow
