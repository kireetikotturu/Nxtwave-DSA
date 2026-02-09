# Middle of the Linked List

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Walmart, Amazon, Google, Intuit, Microsoft, Bloomberg  
**LeetCode:** https://leetcode.com/problems/middle-of-the-linked-list/

---

Given the head of a **singly linked list**, your task is to **return the pointer to the middle node** of the linked list.

If there are **two middle nodes**, return the **second middle node**.

---

### Example 1
**Input:**  
n = 5  
Linked List: 1 → 2 → 3 → 4 → 5  

**Output:**  
3 → 4 → 5  

**Explanation:**  
The middle node of the linked list is `3`.

---

### Example 2
**Input:**  
n = 6  
Linked List: 1 → 2 → 3 → 4 → 5 → 6  

**Output:**  
4 → 5 → 6  

**Explanation:**  
There are two middle nodes (`3` and `4`).  
According to the problem, the **second middle node (`4`)** is returned.

---

### Your Task
Complete the function `middleOfTheLL()` that takes:
- `head` – head of the linked list  

and returns the **middle node** of the linked list.

---

### Constraints
- 1 ≤ n ≤ 1000  
- 0 ≤ data ≤ 1000  

---

### Input Format
- First line: integer `n`, number of nodes  
- Second line: `n` space-separated integers representing the linked list  

---

### Output Format
- Print the elements of the linked list starting from the middle node to the end
