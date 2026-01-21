# Sort Characters by Frequency

**Difficulty:** Medium  
**Time Complexity:** O(N log N)  
**Space Complexity:** O(N)  
**Companies:** Yahoo, Uber, Apple, Amazon, Google, Microsoft, Bloomberg, Adobe, Nvidia, Zoho  

---

You are given a string `s`.  
Your task is to **rearrange the characters** in the string so that characters appear in **descending order of their frequency**.

- Frequency = number of times a character appears
- If multiple characters have the same frequency, **any order is allowed**
- Uppercase and lowercase letters are treated as **different characters**

Return the rearranged string.

---

### Example 1
Input:  
s = "green"

Output:  
"eerng"

**Explanation:**  
- 'e' appears twice  
- 'g', 'r', 'n' appear once  
- Any valid ordering with 'e' first is acceptable

---

### Example 2
Input:  
s = "bookKeeping"

Output:  
"ooeeKikbgnp"

**Explanation:**  
- 'o' and 'e' appear twice  
- Remaining characters appear once  
- Case-sensitive comparison (`k` ≠ `K`)

---

### Your Task
Complete the function `sortCharactersByFrequency()` that returns the string sorted by character frequency.

---

### Constraints
- 1 ≤ s.length ≤ 4 × 10⁵  
- `s` contains uppercase letters, lowercase letters, and digits  

---

### Input Format
- A single line containing the string `s`

---

### Output Format
- A single line containing the rearranged string

---

### LeetCode Link
<a href="https://leetcode.com/problems/sort-characters-by-frequency/" target="_blank">
LeetCode – Sort Characters By Frequency (Problem 451)
</a>
