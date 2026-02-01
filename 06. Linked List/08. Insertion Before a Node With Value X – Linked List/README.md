# Insertion Before a Node With Value X – Linked List

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Amazon, Microsoft, Infosys  

---

You are given a **singly linked list**, an integer `x` representing a **target node value**, and an integer `data`.  
Your task is to **insert a new node with value `data` before the node that contains value `x`** and return the updated head.

### Note
- If the target value `x` is present at the **head**, the new node becomes the new head.
- It is guaranteed that the value `x` exists in the linked list.

---

### Example 1
Input:  
n = 5, x = 3, data = 9  
Linked List: 1 → 2 → 3 → 4 → 5  

Output:  
1 → 2 → 9 → 3 → 4 → 5  

**Explanation:**  
The value `9` is inserted before the node containing value `3`.

---

### Example 2
Input:  
n = 3, x = 1, data = 6  
Linked List: 1 → 2 → 3  

Output:  
6 → 1 → 2 → 3  

**Explanation:**  
Since `x` is present at the head, the new node becomes the new head.

---

### Your Task
Complete the function `insertionBeforeX()` that takes:
- `head` – head of the linked list  
- `x` – target node value  
- `data` – value of the new node  

and returns the **head of the modified linked list**.

---

### Constraints
- 0 ≤ n ≤ 4000  
- 1 ≤ value of node, x ≤ 10⁴  
- 0 ≤ data ≤ 2000  

---

### Input Format
- First line: three integers `n`, `x`, and `data`
- Second line: `n` space-separated integers representing the linked list

---

### Output Format
- Print the elements of the linked list after insertion
