# Cycle Detection in a Linked List

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Microsoft, Oracle, Yahoo, Amazon, Google, Bloomberg  

---

Given a **singly linked list** of integers, determine whether the linked list contains a **cycle**.

A cycle occurs when a node’s `next` pointer points back to a **previous node** in the list, forming a loop.

---

### Example 1
Input:  
n = 4, pos = 1  
Linked List: 3 → 2 → 0 → -4  
Tail connects to node at index `1`

Output:  
true  

**Explanation:**  
The linked list contains a cycle because the last node points back to node `2`.

---

### Example 2
Input:  
n = 3, pos = -1  
Linked List: 1 → 2 → 3  

Output:  
false  

**Explanation:**  
The linked list does not contain any cycle.

---

### Your Task
Implement the function `cycleDetection()` that takes:
- `head` – head of the linked list  

and returns:
- `true` if the linked list contains a cycle  
- `false` otherwise

---

### Constraints
- 1 ≤ n ≤ 10⁵  
- -10⁸ ≤ data ≤ 10⁸  
- `pos` is `-1` or a valid index (0-based indexing)  

**Note:**  
`pos` is used only to create the cycle and is **not passed** to the function.

---

### Input Format
- First line: two integers `n` and `pos`  
- Second line: `n` space-separated integers representing node values  

---

### Output Format
- Print `true` if the linked list contains a cycle, otherwise `false`

---

### LeetCode Link
<a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank">
LeetCode – Linked List Cycle (Problem 141)
</a>
