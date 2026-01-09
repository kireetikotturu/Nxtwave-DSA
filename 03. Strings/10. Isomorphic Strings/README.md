# Isomorphic Strings

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  
**Companies:** Oracle, Amazon, Yandex, Google, Microsoft, LinkedIn, Bloomberg  

---

You are given two strings `s1` and `s2`.  
Your task is to determine whether the two strings are **isomorphic**.

Two strings are considered **isomorphic** if the characters in `s1` can be replaced to get `s2` such that:
- Each character maps to **only one character**
- The mapping is **consistent**
- No two different characters map to the same character
- Order of characters is preserved

### Example 1
Input:  
s1 = "moon"  
s2 = "feed"

Output:  
true

**Explanation:**  
m → f  
o → e  
n → d  
All mappings are consistent.

### Example 2
Input:  
s1 = "ghee"  
s2 = "fear"

Output:  
false

**Explanation:**  
The character `e` maps to two different characters (`a` and `r`).

### Example 3
Input:  
s1 = "abc"  
s2 = "dee"

Output:  
false

**Explanation:**  
Two different characters (`b` and `c`) map to the same character (`e`), which is not allowed.

### Your Task
Complete the function `isomorphic()` that checks whether two strings are isomorphic.

### Constraints
- 1 ≤ s1.length ≤ 10³  
- s1.length == s2.length  
- Strings may contain any valid ASCII characters  

### Input Format
- First line: string `s1`
- Second line: string `s2`

### Output Format
- Print `true` if the strings are isomorphic, otherwise print `false`

### LeetCode Link
<a href="https://leetcode.com/problems/isomorphic-strings/" target="_blank">
LeetCode – Isomorphic Strings (Problem 205)
</a>
