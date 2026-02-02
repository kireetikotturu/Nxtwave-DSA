# Delete Kth Node of the Linked List

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Samsung  
**LeetCode:** Not Available  

---

You are given a **singly linked list** and an integer `k` (0-based indexing).  
Your task is to **delete the k-th node from the beginning** of the linked list and return the updated head.

---

### Note
- Indexing is **0-based**
- If `k = 0`, the head node should be deleted
- If `k` is greater than or equal to the number of nodes, the list remains unchanged

---

### Example 1
**Input:**  
n = 5, k = 3  
Linked List: 1 → 2 → 3 → 4 → 5  

**Output:**  
1 → 2 → 3 → 5  

**Explanation:**  
The node at index `3` (value `4`) is removed.

---

### Example 2
**Input:**  
n = 4, k = 1  
Linked List: 10 → 20 → 30 → 40  

**Output:**  
10 → 30 → 40  

**Explanation:**  
The node at index `1` (value `20`) is deleted.

---

### Your Task
Complete the function `deleteKthNode()` that takes:
- `head` – head of the linked list  
- `k` – index of the node to be deleted  

and returns the **head of the modified linked list**.

---

### Constraints
- 0 ≤ n, k ≤ 9000  
- 1 ≤ data ≤ 1000  

---

### Input Format
- First line: two integers `n` and `k`  
- Second line: `n` space-separated integers representing the linked list  

---

### Output Format
- Print the elements of the linked list after deleting the k-th node
