# Filter Linked List Nodes by Array

**Difficulty:** Medium  
**Time Complexity:** O(n + m)  
**Space Complexity:** O(m)  
**Companies:** Amazon, Google  
**LeetCode:** Not Available  

---

You are given a **singly linked list** and an integer array `arr` of size `m`.

Your task is to **delete all nodes from the linked list whose values are present in the array `arr`** and return the modified linked list.

---

### Note
- All values in `arr` are **unique**
- Every value in `arr` **exists in the linked list**
- All occurrences of values present in `arr` must be removed

---

### Example 1
**Input:**  
arr = [6, 9]  
Linked List: 5 → 6 → 7 → 8 → 9  

**Output:**  
5 → 7 → 8  

**Explanation:**  
Nodes with values `6` and `9` are removed.

---

### Example 2
**Input:**  
arr = [2, 4, 5]  
Linked List: 1 → 2 → 3 → 4 → 5  

**Output:**  
1 → 3  

**Explanation:**  
All nodes with values `2`, `4`, and `5` are deleted.

---

### Your Task
Complete the function `deleteNodes()` that takes:
- `head` – head of the linked list  
- `arr` – array of values to be removed  

and returns the **head of the modified linked list**.

---

### Constraints
- 1 ≤ n ≤ 10³  
- 1 ≤ m ≤ 10³  
- -10⁴ ≤ data ≤ 10⁴  
- -10⁴ ≤ arr[i] ≤ 10⁴  

---

### Input Format
- First line: integer `m` (size of array `arr`)
- Second line: `m` space-separated integers
- Third line: integer `n` (number of nodes)
- Fourth line: `n` space-separated integers (linked list values)

---

### Output Format
- Print the updated linked list as space-separated integers after deletion
