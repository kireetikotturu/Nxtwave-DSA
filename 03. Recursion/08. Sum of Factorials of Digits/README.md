# Sum of Factorials of Digits

**Difficulty:** Medium  
**Time Complexity:** O(d × f)  
**Space Complexity:** O(d)  

---

You're given a positive integer `n`.  
Your task is to calculate the **sum of the factorials of each digit** of the given number using **recursion**.

Here, `d` is the number of digits in `n`, and `f` is the cost of computing factorial (bounded since digits are 0–9).

### Example 1
Input:  
n = 123  

Output:  
9  

**Explanation:**  
1! + 2! + 3! = 1 + 2 + 6 = 9

### Example 2
Input:  
n = 95  

Output:  
363000  

**Explanation:**  
9! + 5! = 362880 + 120 = 363000

### Your Task
Complete the function `sumOfFactorialsOfDigits()` that takes an integer `n` as an argument and returns the sum of the factorials of its digits using recursion.

### Constraints
- 1 ≤ n ≤ 10⁹  

### Input Format
- The input consists of a single integer `n`.

### Output Format
- Output is a single integer representing the sum of the factorials of the digits of `n`.
