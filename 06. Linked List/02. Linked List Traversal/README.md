# Linked List Traversal

**Difficulty:** Easy  
**Approach:** Iterative Traversal using Pointer  
**Time Complexity:** O(N)  
**Space Complexity:** O(N) (for output storage)  
**Success Rate:** 87%  

---

You are given the **head of a singly linked list**.  
Your task is to **traverse the linked list** and **print all elements** in order.

Traversal means visiting each node starting from the head and moving to the next node until the end of the list is reached.

---

### Example 1
Input:  
n = 2  
Linked List: 10 → 20  

Output:  
10 20  

**Explanation:**  
Starting from the head, print each node’s data until the end of the list.

---

### Example 2
Input:  
n = 5  
Linked List: 10 → 20 → 30 → 40 → 50  

Output:  
10 20 30 40 50  

**Explanation:**  
All elements of the linked list are printed in order.

---

### Your Task
Complete the function `traversal()` that takes:
- `head` → pointer to the head of the linked list  

and prints all elements of the linked list separated by spaces.

---

### Constraints
- 0 ≤ n ≤ 4000  
- 1 ≤ data ≤ 1000  

---

### Input Format
- First line: integer `n`
- Second line: `n` space-separated integers representing node values

---

### Output Format
- Print all linked list elements in one line separated by spaces
