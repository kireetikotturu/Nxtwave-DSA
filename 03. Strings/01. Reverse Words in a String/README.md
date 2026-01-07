# Reverse Words in a String

**Difficulty:** Medium  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  
**Companies:** Apple, Amazon, Google, Microsoft, Nvidia, Bloomberg  

---

You are given a string `text`.  
Your task is to **reverse the order of words** in the string.

A **word** is defined as a continuous sequence of non-space characters.

### Note
- The input string may contain **leading or trailing spaces**.
- There may be **multiple spaces between words**.
- The output must contain:
  - **Only one space** between words
  - **No leading or trailing spaces**

### Example 1
Input:  
text = `"The quick brown fox"`

Output:  
`"fox brown quick The"`

**Explanation:**  
The order of words is reversed.

### Example 2
Input:  
text = `" this is a test message "`

Output:  
`"message test a is this"`

**Explanation:**  
Leading and trailing spaces are removed before reversing.

### Example 3
Input:  
text = `"Welcome to    NXTWAVE  "`

Output:  
`"NXTWAVE to Welcome"`

**Explanation:**  
Extra spaces are removed and words are reversed.

### Your Task
Complete the function `reverseWords()` that takes a string `text` and returns a string with words in reverse order following the above rules.

### Constraints
- 1 ≤ text.length ≤ 10⁴  
- `text` contains English letters (upper-case and lower-case), digits, and spaces  
- The string contains **at least one word**

### Input Format
- A single line containing the string `text`

### Output Format
- A single line containing the reversed-word string

### LeetCode Link
<a href="https://leetcode.com/problems/reverse-words-in-a-string/" target="_blank">
LeetCode – Reverse Words in a String (Problem 151)
</a>
