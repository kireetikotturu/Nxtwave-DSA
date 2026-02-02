# Delete Tail of the Linked List

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Samsung  
**LeetCode:** Not Available  

---

You are given a **singly linked list**, and your task is to **delete the node at the end (tail)** of the linked list and return the updated head.

---

### Note
- If the linked list is empty or contains only one node, the list becomes empty after deletion.
- Deleting the tail means the **second last node becomes the new tail**.

---

### Example 1
**Input:**  
n = 5  
Linked List: 1 → 2 → 3 → 4 → 5  

**Output:**  
1 → 2 → 3 → 4  

**Explanation:**  
The last node `5` is removed from the linked list.

---

### Example 2
**Input:**  
n = 1  
Linked List: 10  

**Output:**  
(empty list)

**Explanation:**  
The only node is deleted, so the linked list becomes empty.

---

### Your Task
Complete the function `deleteTail()` that takes:
- `head` – head of the linked list  

and returns the **head of the modified linked list** after deleting the tail node.

---

### Constraints
- 0 ≤ n ≤ 9000  
- 1 ≤ data ≤ 1000  

---

### Input Format
- First line: integer `n`, number of nodes  
- Second line: `n` space-separated integers representing the linked list  

---

### Output Format
- Print the elements of the linked list after deleting the tail node
