# Double Factorial of a Number

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  

---

You're given a positive integer `n`.  
Your task is to calculate the **double factorial** of `n` using **recursion**.

### Note
- If `n` is **odd**, multiply all odd numbers from `1` to `n`.
- If `n` is **even**, multiply all even numbers from `2` to `n`.

### Example 1
Input:  
n = 5  

Output:  
15  

**Explanation:**  
Double factorial of 5 = 5 × 3 × 1 = 15

### Example 2
Input:  
n = 6  

Output:  
48  

**Explanation:**  
Double factorial of 6 = 6 × 4 × 2 = 48

### Your Task
Complete the function `doubleFactorial()` that takes an integer `n` as an argument and returns the double factorial of `n` using recursion.

### Constraints
- 1 ≤ n ≤ 15  

### Input Format
- The input consists of a single integer `n`.

### Output Format
- Output is a single integer representing the double factorial of `n`.
