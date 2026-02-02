# Delete Head of the Linked List

**Difficulty:** Easy  
**Time Complexity:** O(1)  
**Space Complexity:** O(1)  
**Companies:** Samsung  
**LeetCode:** Not Available  

---

You are given a **singly linked list**, and your task is to **delete the node at the beginning (head)** of the linked list and return the updated head.

---

### Note
- If the linked list is empty, return `None`.
- Deleting the head means the **second node becomes the new head**.

---

### Example 1
**Input:**  
n = 5  
Linked List: 1 → 2 → 3 → 4 → 5  

**Output:**  
2 → 3 → 4 → 5  

**Explanation:**  
The head node `1` is removed. The new head is `2`.

---

### Example 2
**Input:**  
n = 1  
Linked List: 10  

**Output:**  
(empty list)

**Explanation:**  
After deleting the only node, the linked list becomes empty.

---

### Your Task
Complete the function `deleteHead()` that takes:
- `head` – head of the linked list  

and returns the **head of the modified linked list** after deleting the first node.

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
- Print the elements of the linked list after deleting the head node
