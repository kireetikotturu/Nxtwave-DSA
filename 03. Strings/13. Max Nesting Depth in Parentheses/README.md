# Max Nesting Depth in Parentheses

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  
**Companies:** Intel, Microsoft, Bloomberg  

---

You are given a string `s` consisting of digits and arithmetic characters along with parentheses `(` and `)`.

Your task is to determine the **maximum nesting depth of parentheses** in the string.

**Nesting depth** refers to the highest number of parentheses that are nested inside each other at any point in the string.

---

### Example 1
Input:  
s = "(3 + (2*5) + (1 + (4/2)) + 2)"

Output:  
3

Explanation:  
- Level 1: (3 + (2*5) + (1 + (4/2)) + 2)  
- Level 2: (2*5), (1 + (4/2))  
- Level 3: (4/2)  
Maximum depth = 3

---

### Example 2
Input:  
s = "(4) + ((5))"

Output:  
2

Explanation:  
- Level 1: (4), ((5))  
- Level 2: (5)  
Maximum depth = 2

---

### Your Task
Implement the function `maxNestingDepth(s)` that returns the maximum nesting depth of parentheses in the string.

---

### Constraints
- 1 ≤ length of `s` ≤ 100  
- `s` contains digits (0–9), characters `+ - * /`, and parentheses `(`, `)`  
- The string `s` is a valid parentheses string  

---

### Input Format
- A single line containing the string `s`

---

### Output Format
- A single integer representing the maximum nesting depth of parentheses

---

### LeetCode Link (Related)
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
