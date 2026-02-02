# Delete Node With Value X – Linked List

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Apple, Amazon, Google, Microsoft, Adobe, Bloomberg  
**LeetCode:** Not Available  

---

You are given a **singly linked list** and an integer `x`, denoting the value of a node that needs to be deleted.

Your task is to **remove the first node whose value is equal to `x`** from the linked list and return the updated head.

---

### Note
- Only the **first occurrence** of value `x` should be deleted
- If the value `x` is not present, the linked list remains unchanged
- If the head node contains value `x`, the head should be updated

---

### Example 1
**Input:**  
n = 5, x = 3  
Linked List: 1 → 2 → 3 → 4 → 5  

**Output:**  
1 → 2 → 4 → 5  

**Explanation:**  
The first node with value `3` is removed from the list.

---

### Example 2
**Input:**  
n = 4, x = 8  
Linked List: 1 → 3 → 5 → 8  

**Output:**  
1 → 3 → 5  

**Explanation:**  
The node with value `8` is deleted.

---

### Your Task
Complete the function `deleteNodeWithValueX()` that takes:
- `head` – head of the linked list  
- `x` – value of the node to be deleted  

and returns the **head of the modified linked list**.

---

### Constraints
- 0 ≤ n ≤ 9000  
- 1 ≤ data, x ≤ 1000  

---

### Input Format
- First line: two integers `n` and `x`  
- Second line: `n` space-separated integers representing the linked list  

---

### Output Format
- Print the elements of the linked list after deleting the node with value `x`
