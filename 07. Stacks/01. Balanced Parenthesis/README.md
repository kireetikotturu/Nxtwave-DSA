# Balanced Parenthesis

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  
**Companies:** IBM, Apple, Amazon, Google, Microsoft, LinkedIn, Bloomberg  

---

You are given a string `s` consisting only of the characters:
`(`, `)`, `{`, `}`, `[`, `]`.

Your task is to check whether the string forms a **valid sequence of brackets**.

A sequence is considered **valid** if:
- Every opening bracket has a matching closing bracket of the same type
- Brackets are closed in the **correct order**
- Each closing bracket corresponds to the **most recent unmatched opening bracket**

### Example 1
Input:  
s = "{}()[]"

Output:  
true

**Explanation:**  
All brackets are correctly matched and properly nested.

### Example 2
Input:  
s = "(){[{}])"

Output:  
false

**Explanation:**  
The brackets `{` and `)` do not form a matching pair.

### Your Task
Complete the function `balancedParentheses()` that determines whether the given string is valid.

### Constraints
- 1 ≤ s.length ≤ 1000  
- `s` contains only `(`, `)`, `{`, `}`, `[`, `]`

### Input Format
- A single line containing the string `s`

### Output Format
- Print `true` if the string has balanced parentheses, otherwise print `false`

### LeetCode Link
<a href="https://leetcode.com/problems/valid-parentheses/" target="_blank">
LeetCode – Valid Parentheses (Problem 20)
</a>
