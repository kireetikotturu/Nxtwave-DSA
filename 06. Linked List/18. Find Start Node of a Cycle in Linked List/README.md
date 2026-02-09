# Find Start Node of a Cycle in Linked List

**Difficulty:** Medium  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Yahoo, PayTM, Apple, Amazon, Google, Microsoft, Adobe, Nvidia, Bloomberg  
**LeetCode:** https://leetcode.com/problems/linked-list-cycle-ii/

---

You are given the head of a **singly linked list** that may or may not contain a **cycle**.

Your task is to **return the node where the cycle begins** if a cycle exists.  
If there is **no cycle**, return `NULL`.

---

### Note
A linked list has a cycle if a node points back to a **previous node** instead of pointing to `NULL`.

---

### Example 1
**Input:**  
n = 7, start = 3  
Linked List: 1 → 2 → 3 → 4 → 5 → 6 → 7  
Tail connects to node with value `4`

**Output:**  
4

**Explanation:**  
The linked list contains a cycle starting at the node with value `4`.

---

### Example 2
**Input:**  
n = 5, start = -1  
Linked List: 1 → 2 → 3 → 4 → 5  

**Output:**  
NULL

**Explanation:**  
There is no cycle in the linked list.

---

### Your Task
Complete the function `startNodeCycle()` that takes:
- `head` – head of the linked list  

and returns:
- The **node where the cycle begins**, if a cycle exists  
- `NULL`, if no cycle exists

---

### Constraints
- 1 ≤ n ≤ 10³  
- −10⁴ ≤ data ≤ 10⁴  

---

### Input Format
- First line: two integers `n` and `start`  
  - `start` indicates the index where the cycle begins  
  - `start = -1` means no cycle  
- Second line: `n` space-separated integers representing the linked list

---

### Output Format
- Print the **node value** where the cycle begins  
- Print `NULL` if no cycle exists
