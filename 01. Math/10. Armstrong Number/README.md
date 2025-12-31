# Armstrong Number

**Difficulty:** Medium  
**Time Complexity:** O(log₁₀N)  
**Space Complexity:** O(1)  

---

You are given an integer `num`.  
Your task is to determine whether it is an **Armstrong number** or not.

### Note
A positive number of `n` digits is said to be an Armstrong number if the sum of its digits each raised to the power `n` is equal to the number itself.

### Example 1
Input:  
num = 371  

Output:  
true  

**Explanation:**  
3³ + 7³ + 1³ = 27 + 343 + 1 = 371  
Hence, `371` is an Armstrong number.

### Example 2
Input:  
num = 1296  

Output:  
false  

**Explanation:**  
1⁴ + 2⁴ + 9⁴ + 6⁴ = 7874  
Since this is not equal to `1296`, it is not an Armstrong number.

### Your Task
Complete the function `checkArmstrongNumber()` that takes an integer `num` as its argument and returns `true` if the number is an Armstrong number, otherwise `false`.

### Constraints
- 1 ≤ num ≤ 10⁹  

### Input Format
- Input is a single line consisting of an integer `num`.

### Output Format
- Output is a single line containing `true` if `num` is an Armstrong number, otherwise `false`.

### LeetCode Link
<a href="https://leetcode.com/problems/armstrong-number/" target="_blank">LeetCode – Armstrong Number (Problem 1134)</a>
