"""
Problem: Insertion At Kth Position - Linked List
Approach: Traverse till (k-1)th node and insert the new node
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def insertionAtKthPosition(self, head, k, data):
        # Insert at head
        if k == 0:
            return Node(data, head)

        temp = head
        count = 0

        # Traverse to (k-1)th node
        while temp:
            if count == k - 1:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next
            count += 1

        return head
