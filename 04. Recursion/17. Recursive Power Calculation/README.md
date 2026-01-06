# Recursive Power Calculation

**Difficulty:** Medium  
**Time Complexity:** O(log b)  
**Space Complexity:** O(log b)  

---

You're given a real number `a` and a positive integer `b`.  
Your task is to compute **a raised to the power b (aᵇ)** using **recursion**.

This solution uses an **optimized recursive approach** known as **Exponentiation by Squaring**.

### Example 1
Input:  
a = 2  
b = 3  

Output:  
8.000  

**Explanation:**  
2³ = 2 × 2 × 2 = 8.000

### Example 2
Input:  
a = 5  
b = 4  

Output:  
625.000  

**Explanation:**  
5⁴ = 5 × 5 × 5 × 5 = 625.000

### Your Task
Complete the function `recursivePower()` that takes:
- a real number `a`
- an integer `b` (b > 0)

and returns the value of `a` raised to the power `b` using recursion.

### Constraints
- 0 ≤ a ≤ 10  
- 1 ≤ b ≤ 10  

### Input Format
- First line: a double value `a`
- Second line: an integer value `b`

### Output Format
- Output the value of `aᵇ` rounded to **three decimal places**.
