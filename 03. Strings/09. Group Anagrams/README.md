# Group Anagrams

**Difficulty:** Medium  
**Time Complexity:** O(N × K)  
**Space Complexity:** O(N × K)  
**Companies:** Salesforce, Oracle, Walmart, Apple, Amazon, Google, Microsoft, Bloomberg  

---

You are given an array of strings `strs`.  
Your task is to **group all anagrams together**.

An **anagram** is a word formed by rearranging the letters of another word using all original letters exactly once.

### Example 1
Input:  
strs = ["act", "cat", "pit", "tac", "tip", "tab"]

Output:  
["act", "cat", "tac"]  
["pit", "tip"]  
["tab"]

**Explanation:**  
- "act", "cat", and "tac" are anagrams  
- "pit" and "tip" are anagrams  
- "tab" has no anagram pair  

### Example 2
Input:  
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:  
["eat", "tea", "ate"]  
["tan", "nat"]  
["bat"]

### Your Task
Complete the function `groupAnagrams()` that groups strings that are anagrams of each other.

### Constraints
- 1 ≤ strs.length ≤ 10⁴  
- 1 ≤ strs[i].length ≤ 100  
- Strings contain only lowercase English letters  

### Input Format
- First line: integer `n` (number of strings)
- Second line: `n` space-separated strings

### Output Format
- Output the grouped anagrams (order does not matter)

### LeetCode Link
<a href="https://leetcode.com/problems/group-anagrams/" target="_blank">
LeetCode – Group Anagrams (Problem 49)
</a>
