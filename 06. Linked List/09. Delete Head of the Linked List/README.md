Delete Head of the Linked List
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
Companies: Samsung

You are given a linked list, and your task is to delete the node at the beginning (head) of the list.

After deleting the head node, return the new head of the linked list.

Note
If the linked list is empty, return None.

Example 1
Input:
n = 5
Linked List = [1, 2, 3, 4, 5]

Output:
2 3 4 5

Explanation:
The head node (1) is removed. The new head is 2.

Example 2
Input:
n = 1
Linked List = [10]

Output:
(empty list)

Explanation:
The only node in the list is deleted, so the list becomes empty.

Your Task
Complete the provided deleteHead function that takes the head of the linked list and returns the head of the modified list after deleting the first node.

Constraints
0 ≤ n ≤ 9000
1 ≤ data ≤ 1000

Input Format
The first line contains an integer n, representing the number of nodes in the linked list.
The second line contains n space-separated integers representing the linked list.

Output Format
Print the elements of the linked list after deleting the head node.
