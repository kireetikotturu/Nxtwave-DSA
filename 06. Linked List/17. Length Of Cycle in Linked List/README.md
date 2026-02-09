# Length Of Cycle in Linked List

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Qualcomm, Amazon, Adobe  
**LeetCode:** https://leetcode.com/problems/linked-list-cycle-ii/  

---

You are given a **singly linked list** where the last node may either point to `null` or back to a node within the list, forming a **cycle**.

Your task is to **detect whether a cycle exists** in the linked list.  
- If a cycle is present, **return the length of the cycle**.  
- If no cycle exists, **return `0`**.

---

### Example 1
**Input:**  
n = 8, pos = 2  
Linked List: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8  
Tail connects to node at index `2`

**Output:**  
6

**Explanation:**  
The cycle starts at node `3` and includes 6 nodes.

---

### Example 2
**Input:**  
n = 5, pos = -1  
Linked List: 1 → 2 → 3 → 4 → 5  

**Output:**  
0

**Explanation:**  
There is no cycle in the linked list.

---

### Your Task
Complete the function `lengthOfCycle()` that takes:
- `head` – head of the linked list  

The function should:
- Return the **length of the cycle** if one exists  
- Return **0** if no cycle is present

---

### Constraints
- 1 ≤ n ≤ 90,000  
- 1 ≤ data ≤ 10⁸  
- `pos` is `-1` or a valid index (0-based)  
- `pos` is **not passed** as a parameter

---

### Input Format
- First line: two integers `n` and `pos`  
- Second line: `n` space-separated integers representing the linked list

---

### Output Format
- Print a single integer representing the **length of the cycle**  
- Print `0` if no cycle exists
