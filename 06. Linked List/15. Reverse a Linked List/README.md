# Reverse a Linked List

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** ByteDance, Oracle, Uber, Yelp, Apple, Amazon, Yahoo, Google, Zenefits, SAP, Microsoft, Adobe, Nvidia, Bloomberg  

---

Given the head of a **singly linked list** of integers, your task is to **reverse the linked list** and return the head pointer of the modified linked list.

---

### Example 1
Input:  
n = 5  
Linked List: 1 → 2 → 3 → 4 → 5  

Output:  
5 → 4 → 3 → 2 → 1  

**Explanation:**  
The linked list is reversed by changing the direction of the pointers.

---

### Example 2
Input:  
n = 3  
Linked List: 10 → 20 → 30  

Output:  
30 → 20 → 10  

**Explanation:**  
After reversing, the last node becomes the head.

---

### Your Task
Complete the provided `reverseLL` function that takes:
- `head` – head of the linked list  

and returns the **head of the reversed linked list**.

---

### Constraints
- 1 ≤ n ≤ 9000  
- 0 ≤ data ≤ 10⁵  

---

### Input Format
- The first line contains an integer `n`, representing the number of nodes in the linked list.  
- The second line consists of `n` space-separated integers representing the linked list.

---

### Output Format
- The output is a single line containing the values of the nodes in the reversed linked list, space-separated.

---

### LeetCode Link
<a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank">
LeetCode – Reverse Linked List (Problem 206)
</a>
