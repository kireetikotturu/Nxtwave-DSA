# Remove All Adjacent Duplicates In String

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  
**Companies:** Google, Amazon, Microsoft, Apple  

---

You are given a string `s` consisting of lowercase English letters.

A duplicate removal consists of choosing two **adjacent and equal** letters and removing them.

This process is repeated until no more duplicate removals are possible.

It is guaranteed that the final result is **unique**.

---

### Example 1
Input:  
s = "abbaca"

Output:  
"ca"

**Explanation:**  
- Remove "bb" → "aaca"  
- Remove "aa" → "ca"

---

### Example 2
Input:  
s = "azxxzy"

Output:  
"ay"

**Explanation:**  
- Remove "xx" → "azzy"  
- Remove "zz" → "ay"

---

### Approach
Use a **stack** to process characters:
- If the current character is the same as the top of the stack → remove it
- Otherwise → push it into the stack

At the end, the stack contains the final string.

---

### Constraints
- 1 ≤ s.length ≤ 10⁵  
- s contains only lowercase English letters  

---

### Input Format
- A single string `s`

---

### Output Format
- A single string after removing all adjacent duplicates

---

### LeetCode Link
<a href="https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/" target="_blank">
LeetCode – Remove All Adjacent Duplicates In String (Problem 1047)
</a>

