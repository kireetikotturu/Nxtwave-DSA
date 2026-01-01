# Sum of Digits Until Single Digit

**Difficulty:** Medium  
**Time Complexity:** O(1)  
**Space Complexity:** O(1)  

---

You are given an integer `num`.  
Your task is to find the **sum of its digits repeatedly until the result becomes a single digit**.

### Example 1
Input:  
num = 4591  

Output:  
1  

**Explanation:**  
Start with 4591  
→ 4 + 5 + 9 + 1 = 19  
→ 1 + 9 = 10  
→ 1 + 0 = 1 (single digit)  

So, the final answer is `1`.

### Example 2
Input:  
num = 5674  

Output:  
4  

**Explanation:**  
Start with 5674  
→ 5 + 6 + 7 + 4 = 22  
→ 2 + 2 = 4 (single digit)  

So, the final answer is `4`.

### Your Task
Complete the function `sumOfDigits()` that takes an integer `num` as an argument and returns the sum of digits until the result becomes a single digit.

### Constraints
- 1 ≤ num ≤ 10⁹  

### Input Format
- Input is a single line consisting of an integer `num`.

### Output Format
- Output is a single integer representing the final single-digit sum.

### LeetCode Link
<a href="https://leetcode.com/problems/add-digits/" target="_blank">LeetCode – Add Digits (Problem 258)</a>
