# Insertion At Tail – Linked List

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Amazon, Microsoft, Infosys  

---

You are given a **singly linked list** and an integer value `a`.  
Your task is to **insert a new node with value `a` at the end (tail)** of the linked list and return the updated head.

### Note
Insertion at the tail means the new node becomes the **last node** of the linked list.

---

### Example 1
Input:  
n = 3, a = 4  
Linked List: 1 → 2 → 3  

Output:  
1 → 2 → 3 → 4  

**Explanation:**  
The value `4` is inserted at the end of the linked list.

---

### Example 2
Input:  
n = 2, a = 2  
Linked List: 5 → 7  

Output:  
5 → 7 → 2  

**Explanation:**  
The value `2` is inserted at the tail of the linked list.

---

### Your Task
Complete the function `insertionAtTail()` that takes:
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
- Print the elements of the modified linked list after insertion at tail
