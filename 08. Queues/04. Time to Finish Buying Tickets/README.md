# Time to Finish Buying Tickets

**Difficulty:** Medium  
**Time Complexity:** O(N × T)  
**Space Complexity:** O(N)  
**Companies:** Amazon, Google, Microsoft  

---

There are `n` people standing in a queue to buy tickets.

- The person at the **front** of the queue is at index `0`
- The person at the **back** is at index `n - 1`

You are given a **0-indexed array** `tickets`, where  
`tickets[i]` represents the number of tickets the `i-th` person wants.

---

### Rules
- Each person takes **1 second** to buy **1 ticket**
- If a person still needs more tickets, they move to the **back of the queue**
- If a person finishes buying tickets, they **leave the queue**

---

### Goal
Determine the **total time** it takes for the person initially at index `k`
to finish buying all their tickets.

---

### Example 1
Input:  
tickets = [2, 3, 2]  
k = 2  

Output:  
6  

---

### Example 2
Input:  
tickets = [5, 1, 1, 1]  
k = 0  

Output:  
8  

---

### Your Task
Complete the function `calculateTime()` that returns the total time
required for the person at index `k` to finish buying tickets.

---

### Constraints
- 1 ≤ n ≤ 200  
- 1 ≤ tickets[i] ≤ 200  
- 0 ≤ k < n  

---

### Input Format
- First line: integer `n`
- Second line: `n` space-separated integers (`tickets`)
- Third line: integer `k`

---

### Output Format
- Single integer representing the total time

---

### LeetCode Link
<a href="https://leetcode.com/problems/time-needed-to-buy-tickets/" target="_blank">
LeetCode – Time Needed to Buy Tickets (Problem 2073)
</a>
