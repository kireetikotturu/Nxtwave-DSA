# Insertion At Head – Linked List

**Difficulty:** Easy  
**Time Complexity:** O(1)  
**Space Complexity:** O(1)  
**Companies:** Amazon, Microsoft, Infosys  

---

You are given a **singly linked list** and an integer value `a`.  
Your task is to **insert a new node with value `a` at the beginning (head)** of the linked list and return the updated head.

### Note
Insertion at the head means the new node becomes the **first node** of the linked list.

---

### Example 1
Input:  
n = 3, a = 4  
Linked List: 1 → 2 → 3  

Output:  
4 → 1 → 2 → 3  

**Explanation:**  
The value `4` is inserted at the beginning of the linked list.

---

### Example 2
Input:  
n = 2, a = 2  
Linked List: 5 → 7  

Output:  
2 → 5 → 7  

**Explanation:**  
The value `2` is inserted at the head of the linked list.

---

### Your Task
Complete the function `insertionAtHead()` that takes:
- `head` – head of the linked list  
- `a` – value of the new node  

and returns the **head of the modified linked list**.

---

### Constraints
- 0 ≤ n ≤ 9000  
- 0 ≤ a ≤ 2000  
- 1 ≤ data ≤ 1000  

---

### Input Format
- First line: two integers `n` and `a`
- Second line: `n` space-separated integers representing the linked list

---

### Output Format
- Print the elements of the modified linked list after insertion at head
