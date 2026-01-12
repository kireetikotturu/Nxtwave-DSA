# Largest Rectangle in Histogram

**Difficulty:** Hard  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  
**Companies:** Roblox, Apple, Amazon, Zoho, Google, Microsoft, Bloomberg  

---

You are given an array `arr` of length `n` representing the heights of bars in a histogram.  
Each bar has a width of **1 unit**.

Your task is to determine the **largest rectangular area** that can be formed within the histogram.

---

### Example 1
Input:  
n = 6  
arr = [4, 2, 7, 6, 1, 5]

Output:  
12

**Explanation:**  
The largest rectangle is formed by the bars with heights **7 and 6**,  
minimum height = 6, width = 2  
Area = 6 × 2 = 12

---

### Example 2
Input:  
n = 8  
arr = [2, 6, 4, 1, 5, 2, 7, 3]

Output:  
8

**Explanation:**  
- Rectangle using height 1 across all bars → area = 1 × 8 = 8  
- Rectangle using height 4 across 2 bars → area = 4 × 2 = 8  

Maximum area = 8

---

### Your Task
Complete the function `largestRectangleArea()` that returns the maximum rectangular area possible.

---

### Constraints
- 1 ≤ n ≤ 10⁴  
- 0 ≤ arr[i] ≤ 10³  

---

### Input Format
- First line: integer `n`  
- Second line: `n` space-separated integers

---

### Output Format
- A single integer representing the largest rectangle area

---

### LeetCode Link
<a href="https://leetcode.com/problems/largest-rectangle-in-histogram/" target="_blank">
LeetCode – Largest Rectangle in Histogram (Problem 84)
</a>
