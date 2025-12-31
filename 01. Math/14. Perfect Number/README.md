# Perfect Number

**Difficulty:** Easy  
**Time Complexity:** O(√N)  
**Space Complexity:** O(1)  
**Companies:** Facebook, Google, Yahoo, Amazon  

---

You are given an integer `num`.  
Your task is to determine whether it is a **Perfect number** or not.

### Note
A number is said to be **Perfect** if it is equal to the sum of its **proper divisors**
(i.e., sum of all divisors excluding the number itself).

### Example 1
Input:  
num = 6  

Output:  
true  

**Explanation:**  
The proper divisors of `6` are `1`, `2`, and `3`.  
Sum = 1 + 2 + 3 = 6  
Hence, `6` is a perfect number.

### Example 2
Input:  
num = 30  

Output:  
false  

**Explanation:**  
The proper divisors of `30` are `1, 2, 3, 5, 6, 10, 15`.  
Sum = 42, which is not equal to `30`.  
Hence, `30` is not a perfect number.

### Your Task
Complete the function `checkPerfectNumber()` that takes an integer `num` as an argument and returns `true` if the number is perfect, otherwise `false`.

### Constraints
- 1 ≤ num ≤ 10⁹  

### Input Format
- Input is a single line consisting of an integer `num`.

### Output Format
- Output is a single line containing `true` if `num` is a perfect number, otherwise `false`.

### LeetCode Link
<a href="https://leetcode.com/problems/perfect-number/" target="_blank">LeetCode – Perfect Number (Problem 507)</a>
