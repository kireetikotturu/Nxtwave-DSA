# Trapping Rainwater

**Difficulty:** Hard  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  
**Companies:** Oracle, Amazon, Yandex, Google, Microsoft, Bloomberg  

---

You are given an array `arr` of non-negative integers where each element represents
the height of a bar in an **elevation map**.

Each bar has a width of **1 unit**.

Your task is to calculate how much **rainwater can be trapped** between the bars
after it rains.

---

### Note
Water can be trapped between bars only if there are taller bars on both the left
and right sides.

---

### Example
Input:  
n = 11  
arr = [0, 2, 3, 0, 3, 2, 2, 4, 0, 2, 3]

Output:  
9

**Explanation:**  
Total trapped rainwater = **9 units**

---

### Your Task
Complete the function `trapRainwater()` that returns the total units of trapped water.

---

### Constraints
- 1 ≤ n ≤ 5000  
- 0 ≤ arr[i] ≤ 10⁴  

---

### Input Format
- First line: integer `n`
- Second line: `n` space-separated integers

---

### Output Format
- A single integer representing total trapped rainwater

---

### LeetCode Link
<a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank">
LeetCode – Trapping Rain Water (Problem 42)
</a>
