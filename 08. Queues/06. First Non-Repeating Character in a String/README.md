# First Non-Repeating Character in a String

**Difficulty:** Medium  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  
**Companies:** Amazon, Google, Microsoft  

---

You are given a string `s`.  
Your task is to find the **index of the first character that appears only once** in the entire string.

If no such character exists, return `-1`.

The index should be **0-based**.

---

### Example 1
Input:  
s = "success"

Output:  
1

**Explanation:**  
The character `'u'` appears only once and is at index `1`.

---

### Example 2
Input:  
s = "aabbccdd"

Output:  
-1

**Explanation:**  
All characters repeat, so there is no unique character.

---

### Your Task
Complete the function `firstUniqueCharacter()` that returns the index of the first non-repeating character.

---

### Constraints
- 1 ≤ s.length ≤ 10⁵  
- `s` consists of lowercase English letters only  

---

### Input Format
- First line: integer `n` (length of string)  
- Second line: string `s`

---

### Output Format
- Single integer representing the index of the first unique character  
- Return `-1` if none exists

---

### LeetCode Link
<a href="https://leetcode.com/problems/first-unique-character-in-a-string/" target="_blank">
LeetCode – First Unique Character in a String (Problem 387)
</a>
