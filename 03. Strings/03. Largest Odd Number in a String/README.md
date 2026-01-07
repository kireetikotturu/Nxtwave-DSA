# Largest Odd Number in a String

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  
**Companies:** Google, Amazon, Microsoft  

---

You are given a string `s` composed only of numerical characters (`0–9`).  
Your task is to find the **largest non-empty substring** that represents an **odd number**.

### Note
- A substring must be **contiguous**
- If **no odd digit** exists in the string, return an empty string `""`

### Example 1
Input:  
s = "23467850"

Output:  
"2346785"

**Explanation:**  
The largest substring ending with an odd digit is `"2346785"`.

### Example 2
Input:  
s = "6804"

Output:  
""

**Explanation:**  
No odd digit exists in the string.

### Example 3
Input:  
s = "683789"

Output:  
"683789"

**Explanation:**  
The entire string is already an odd number.

### Your Task
Complete the function `largestOddNumber()` that takes a string `s` and returns the largest odd-number substring.

### Constraints
- 1 ≤ n ≤ 10⁴  
- `s` consists only of digits (`0–9`)

### Input Format
- A single line containing the string `s`

### Output Format
- A single line containing the largest odd-number substring

### LeetCode Link
<a href="https://leetcode.com/problems/largest-odd-number-in-string/" target="_blank">
LeetCode – Largest Odd Number in String (Problem 1903)
</a>
