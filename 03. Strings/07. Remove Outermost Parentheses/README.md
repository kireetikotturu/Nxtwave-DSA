# Remove Outermost Parentheses

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  
**Companies:** Uber, Apple, Amazon, Google, Microsoft, Adobe, Bloomberg  

---

You are given a **valid parentheses string** `s`.  
Your task is to remove the **outermost parentheses** from each **primitive substring**.

A **primitive substring** is a non-empty valid parentheses string that **cannot be split further** into smaller valid parentheses strings.

### Example 1
Input:  
s = "(()())(())"

Output:  
"()()()"

**Explanation:**  
- "(()())" → "()()"  
- "(())" → "()"  
Combined result → `"()()()"`

### Example 2
Input:  
s = "(()())(())(()(()))"

Output:  
"()()()()(())"

**Explanation:**  
- "(()())" → "()()"  
- "(())" → "()"  
- "(()(()))" → "()(())"  
Final result → `"()()()()(())"`

### Your Task
Complete the function `removeOutermostParentheses()` that removes the outermost parentheses from each primitive substring.

### Constraints
- 1 ≤ s.length ≤ 10⁴  
- `s[i]` is either `'('` or `')'`  
- `s` is always a valid parentheses string  

### Input Format
- A single line containing the string `s`

### Output Format
- A single line containing the resulting string

### LeetCode Link
<a href="https://leetcode.com/problems/remove-outermost-parentheses/" target="_blank">
LeetCode – Remove Outermost Parentheses (Problem 1021)
</a>
