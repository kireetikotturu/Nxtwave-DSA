# Elimination Game

**Difficulty:** Medium  
**Time Complexity:** O(log N)  
**Space Complexity:** O(log N)  
**Companies:** Google, Amazon, Microsoft, Apple  

---

You are given a list `arr` containing all integers from `1` to `n` in increasing order.  
You must repeatedly eliminate numbers using the following rules until only **one number remains**:

### Elimination Rules
1. Remove the first number and every other number from **left to right**.
2. Then remove the rightmost number and every other number from **right to left**.
3. Repeat the above steps alternately until one number remains.

### Example 1
Input:  
n = 9  

Output:  
6  

**Explanation:**  
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
→ remove from left → [2, 4, 6, 8]  
→ remove from right → [2, 6]  
→ remove from left → [6]  

Final remaining number is `6`.

### Example 2
Input:  
n = 1  

Output:  
1  

**Explanation:**  
Only one element exists, so the answer is `1`.

### Your Task
Given an integer `n`, return the **last remaining number** after applying the elimination process.

### Constraints
- 1 ≤ n ≤ 10⁹  

### Input Format
- A single integer `n`.

### Output Format
- Output a single integer representing the last remaining number.

### LeetCode Link
<a href="https://leetcode.com/problems/elimination-game/" target="_blank">
LeetCode – Elimination Game (Problem 390)
</a>
