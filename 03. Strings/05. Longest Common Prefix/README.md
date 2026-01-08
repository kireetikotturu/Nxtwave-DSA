# Longest Common Prefix

**Difficulty:** Easy  
**Time Complexity:** O(N × M)  
**Space Complexity:** O(1)  
**Companies:** Visa, Apple, Amazon, Google, Microsoft, Bloomberg  

---

You are given an array of strings `words`.  
Your task is to find the **longest common prefix** shared by all the strings.

If there is no common prefix, return an empty string `""`.

### Example 1
Input:  
words = ["cloud", "close", "clear", "cluster"]

Output:  
"cl"

**Explanation:**  
All words start with `"cl"`, and it is the longest prefix common to all.

### Example 2
Input:  
words = ["dog", "racecar", "car"]

Output:  
""

**Explanation:**  
The strings do not share any common starting characters.

### Your Task
Complete the function `longest_common_prefix()` that takes an array of strings and returns the longest common prefix.

### Constraints
- 1 ≤ words.length ≤ 200  
- 0 ≤ words[i].length ≤ 200  
- Each word contains only lowercase English letters  

### Input Format
- First line: integer `n` (number of words)
- Next `n` lines: strings representing the words

### Output Format
- A single string representing the longest common prefix

### LeetCode Link
<a href="https://leetcode.com/problems/longest-common-prefix/" target="_blank">
LeetCode – Longest Common Prefix (Problem 14)
</a>
