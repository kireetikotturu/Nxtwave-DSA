# Implement Stack Using Queue

**Difficulty:** Easy  
**Time Complexity:**  
- push → O(N)  
- pop → O(1)  
- top → O(1)  
- empty → O(1)  
- size → O(1)  
**Space Complexity:** O(N)  
**Companies:** Amazon, Google, Microsoft  

---

Design and implement a **Stack using a Queue**.

The implemented stack should support all standard stack operations along with a
`size()` method.

---

### Operations to Support
- `push(x)` → Push element `x` onto the stack  
- `pop()` → Remove the top element  
- `top()` → Return the top element  
- `empty()` → Return `true` if stack is empty, else `false`  
- `size()` → Return number of elements in the stack  

---

### Example
Input:  
push 1  
push 2  
push 3  
top  
pop  
top  
empty  
size  

Output:  
3  
2  
false  
2  

---

### Explanation
- push(1) → Stack = [1]  
- push(2) → Stack = [1, 2]  
- push(3) → Stack = [1, 2, 3]  
- top → 3  
- pop → removes 3  
- top → 2  
- empty → false  
- size → 2  

---

### Your Task
Complete the `Stack / MyStack` class using **only a queue** to implement all stack operations.

---

### Constraints
- 1 ≤ number of operations ≤ 10⁴  
- 1 ≤ x ≤ 10⁴  

---

### Input Format
- First line: integer `N` (number of operations)  
- Next `N` lines: operations  

---

### Output Format
- Output results of `top`, `pop`, `empty`, and `size` operations line by line

---

### LeetCode Link
<a href="https://leetcode.com/problems/implement-stack-using-queues/" target="_blank">
LeetCode – Implement Stack using Queues (Problem 225)
</a>
