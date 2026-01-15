# Circle Elimination Game

**Difficulty:** Medium  
**Time Complexity:** O(N × K)  
**Space Complexity:** O(N)  
**Companies:** Google, Amazon, Microsoft  

---

There are `n` friends sitting in a circle, numbered from `1` to `n` in clockwise order.

The game follows these rules:

1. Start counting from the first friend.
2. Count `k` friends clockwise (wrapping around if needed).
3. The last friend counted is eliminated.
4. The next round starts from the friend immediately clockwise to the eliminated one.
5. Repeat until only **one friend** remains.

Your task is to determine **which friend wins the game**.

---

### Example 1
Input:  
n = 5, k = 3  

Output:  
4  

**Explanation:**  
Elimination order: 3 → 1 → 5 → 2  
Winner: **4**

---

### Example 2
Input:  
n = 6, k = 5  

Output:  
1  

**Explanation:**  
Elimination order: 5 → 4 → 6 → 2 → 3  
Winner: **1**

---

### Your Task
Complete the function `getCircleWinner()` that returns the number of the last remaining friend.

---

### Constraints
- 1 ≤ k ≤ n ≤ 600  

---

### Input Format
- Single line with two integers `n` and `k`

---

### Output Format
- Single integer representing the winner

---

### LeetCode Equivalent
<a href="https://leetcode.com/problems/find-the-winner-of-the-circular-game/" target="_blank">
LeetCode – Find the Winner of the Circular Game (Problem 1823)
</a>
