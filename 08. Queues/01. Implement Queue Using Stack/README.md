# Implement Queue Using Stack

**Difficulty:** Easy  
**Time Complexity:**  
- push → O(N)  
- pop → O(1)  
- front → O(1)  
- back → O(N)  
**Space Complexity:** O(N)  
**Companies:** Amazon, Google, Microsoft, Flipkart  

---

Your task is to **implement a Queue using two Stacks**.

The queue should support the following operations:

- `push(x)` → Add element `x` to the back of the queue  
- `pop()` → Remove the front element  
- `front()` → Return the front element  
- `back()` → Return the last element  
- `size()` → Return the number of elements  
- `empty()` → Return `true` if queue is empty, else `false`

---

### Example

Input:  
push 1  
push 2  
push 3  
front  
back  
pop  
front  
back  
empty  
pop  
pop  
size  

Output:  
1  
3  
2  
3  
false  
0  

---

### Explanation
- push 1 → Queue = [1]  
- push 2 → Queue = [1, 2]  
- push 3 → Queue = [1, 2, 3]  
- front → 1  
- back → 3  
- pop → removes 1  
- front → 2  
- back → 3  
- empty → false  
- pop → removes 2  
- pop → removes 3  
- size → 0  

---

### Your Task
Complete the `MyQueue` class using **two stacks** to support all operations.

---

### Constraints
- 1 ≤ x ≤ 10⁴  
- 1 ≤ number of operations ≤ 10⁴  

---

### Input Format
- First line: integer `n` (number of operations)  
- Next `n` lines: queue operations  

---

### Output Format
- Output results of `front`, `back`, `size`, and `empty` operations line by line

---

### LeetCode Link
<a href="https://leetcode.com/problems/implement-queue-using-stacks/" target="_blank">
LeetCode – Implement Queue using Stacks (Problem 232)
</a>
