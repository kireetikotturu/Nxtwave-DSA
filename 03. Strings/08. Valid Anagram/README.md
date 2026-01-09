# Valid Anagram

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  
**Companies:** Apple, Amazon, Google, Microsoft  

---

You are given two strings `s1` and `s2`.  
Your task is to determine whether `s2` is an **anagram** of `s1`.

An **anagram** is formed by rearranging the letters of one string to create another string, using **every character exactly once**.

### Example 1
Input:  
s1 = "night"  
s2 = "thing"

Output:  
true

**Explanation:**  
Both strings contain the same characters with the same frequencies, only arranged differently.

### Example 2
Input:  
s1 = "hello"  
s2 = "elhoo"

Output:  
false

**Explanation:**  
Character frequencies differ (`l` and `o`), so the strings are not anagrams.

### Your Task
Complete the function `validAnagram()` that checks whether two strings are anagrams.

### Constraints
- 1 ≤ s1.length, s2.length ≤ 10⁵  
- Strings contain only lowercase English letters  

### Input Format
- First line: string `s1`
- Second line: string `s2`

### Output Format
- Print `true` if `s2` is an anagram of `s1`, otherwise print `false`

### LeetCode Link
<a href="https://leetcode.com/problems/valid-anagram/" target="_blank">
LeetCode – Valid Anagram (Problem 242)
</a>
