# Print 1-N & Back with Conditions

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  

---

You're given a positive integer `n`.  
Your task is to write a **recursive function** that:

1. First prints all **even numbers** from `1` to `n` in **ascending order**.
2. Then prints all **odd numbers** from `n` to `1` in **descending order**.

### Example 1
Input:  
n = 5  

Output:  
2 4 5 3 1  

**Explanation:**  
- Even numbers from 1 to 5 → `2 4`  
- Odd numbers from 5 to 1 → `5 3 1`

### Example 2
Input:  
n = 6  

Output:  
2 4 6 5 3 1  

**Explanation:**  
- Even numbers from 1 to 6 → `2 4 6`  
- Odd numbers from 6 to 1 → `5 3 1`

### Your Task
Complete the function `printEvenOdd()` that takes an integer `n` as an argument and prints the numbers from `1` to `n` and from `n` to `1` under the given conditions using recursion.

### Constraints
- 1 ≤ n ≤ 950  

### Input Format
- The input contains a single integer `n`.

### Output Format
- The output represents the numbers printed according to the given conditions.
