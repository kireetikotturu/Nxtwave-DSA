# Insertion At Kth Position – Linked List

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Amazon, Microsoft, Infosys  

---

You are given a **singly linked list**, an integer `k` representing a position (**0-based indexing**), and an integer `data`.  
Your task is to **insert a new node with value `data` at the kth position** in the linked list and return the updated head.

### Note
- Indexing starts from **0**
- If `k = 0`, insertion happens at the **head**
- It is guaranteed that `0 ≤ k ≤ n`

---

### Example 1
Input:  
n = 4, k = 2, data = 6  
Linked List: 1 → 2 → 3 → 4  

Output:  
1 → 2 → 6 → 3 → 4  

**Explanation:**  
The value `6` is inserted at index `2` (3rd position in 0-based indexing).

---

### Example 2
Input:  
n = 4, k = 4, data = 5  
Linked List: 1 → 2 → 3 → 4  

Output:  
1 → 2 → 3 → 4 → 5  

**Explanation:**  
The value `5` is inserted at index `4`, which is the tail of the linked list.

---

### Your Task
Complete the function `insertionAtKthPosition()` that takes:
- `head` – head of the linked list  
- `k` – position to insert the new node (0-based)  
- `data` – value of the new node  

and returns the **head of the modified linked list**.

---

### Constraints
- 0 ≤ k ≤ n ≤ 9000  
- 0 ≤ data ≤ 2000  
- 1 ≤ value of node ≤ 1000  

---

### Input Format
- First line: three integers `n`, `k`, and `data`
- Second line: `n` space-separated integers representing the linked list

---

### Output Format
- Print the elements of the linked list after insertion at the kth position
